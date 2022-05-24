#!/bin/python

from flask import Flask

from fontprinter import app as FontPrinter
from index import app as Index
from secret import add_secret

app = Flask(__name__)
app.register_blueprint(FontPrinter)
app.register_blueprint(Index)

add_secret(app)


@app.after_request
def disable_cache(response):
    response.headers["Cache-Control"] = "no-store"
    response.headers["Expires"] = "0"
    return response
