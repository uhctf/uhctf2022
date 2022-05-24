#!/bin/python3
import json
import sqlite3
from flask import Flask, request, jsonify
import sqlite3
from pathlib import Path


application = Flask(__name__, static_folder="static", static_url_path="")


CONFIG = {'query_parameter': (
    '2RZCQY24IKSHKA67RBZU5L3HKCEEUOIGPLHQ5M6X', 'KLZ5SKGIABDZTFWKD4CL4E5N2SINVGCTXSLYUU2Y')}

DB_PATH = Path(__file__).parents[1] / "database" / "database.db"
DB_PATH = "file:{}?mode=ro".format(DB_PATH)


DBCONN = sqlite3.connect(DB_PATH, uri=True)
DBCONN.row_factory = sqlite3.Row


def get_db_conn():
    global DBCONN
    return DBCONN.cursor()


@application.route("/")
def index():
    return application.send_static_file("index.html")


@application.route("/lookup", methods=["GET"])
def query_db():
    if "q" not in request.args:
        return jsonify({'error': 'no query provided'})

    try:
        cursor = get_db_conn()
        # The correct way to do it:
        # cursor.execute(
        #    "SELECT title, rating, sequel_title, sequel_rating FROM movies WHERE lower_title LIKE ?", ["%{}%".format(request.args["q"].lower())])

        query = "SELECT title, rating, sequel_title, sequel_rating FROM movies WHERE lower_title LIKE '%" + \
            request.args["q"].lower()+"%'"
        cursor.execute(query)

        results = cursor.fetchmany(10)
        results = map(lambda item: dict(item), results)
        return jsonify({'error': 'OK', 'results': list(results)})
    except Exception as e:
        if request.args.get(CONFIG['query_parameter'][0]) == CONFIG['query_parameter'][1]:
            return jsonify({'error': 'SQLite database error', '_DEBUG_MSG': str(e), '_DEBUG_QRY': query}), 500

        return jsonify({'error': 'SQLite database error'}), 500
