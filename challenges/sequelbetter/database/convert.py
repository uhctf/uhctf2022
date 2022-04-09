#!/bin/python
import subprocess
import csv
from pathlib import Path
import json
import ast

import sqlite3
import datetime
import os
import re

# Extract
cwd = Path(__file__).parents[0]

DATE_REGEX = re.compile(r"(\d{4})-(\d{2})-(\d{2})")


def extract_archive():
    subprocess.run(["7z", "x", "moviedb.zip", "-aoa"], cwd=cwd)


def create_collections():
    collections = dict()
    no_collections = []
    all_titles_and_years = set()
    print("Reading data from the CSV")
    with open(cwd / "movies_metadata.csv") as csv_file:
        data = csv.DictReader(csv_file)
        for entry in data:
            if entry["adult"] != "False":
                continue
            if entry["status"] is None:
                continue
            if entry["status"] in ["Planned", "Canceled"]:
                continue
            if entry["vote_count"] == "0" or int(entry["vote_count"]) < 3:
                continue

            regex_match = DATE_REGEX.fullmatch(entry["release_date"])
            if regex_match is None:
                entry["year"] = None
            else:
                entry["release_date"] = datetime.datetime(
                    year=int(regex_match[1]), month=int(regex_match[2]), day=int(regex_match[2]))
                entry["year"] = int(regex_match[1])

            title_tuple = (entry["original_title"], entry["year"])
            while title_tuple in all_titles_and_years:
                entry["original_title"] = entry["original_title"] + " (2)"
                title_tuple = (entry["original_title"], entry["year"])

            all_titles_and_years.add(title_tuple)

            if entry["belongs_to_collection"] == "":
                no_collections.append(entry)
            else:
                decoded_collection = ast.literal_eval(
                    entry["belongs_to_collection"])

                id = decoded_collection["id"]
                if id in collections:
                    collections[id].append(entry)
                else:
                    collections[id] = [entry]
    collections[None] = no_collections
    return collections


def build_database(collections):
    def entry_title(movie):
        return movie["original_title"] + (" ({})".format(movie["year"]) if "year" in movie else "")

    if os.path.isfile(cwd / "database.db"):
        print("Remove existing database…")
        os.remove(cwd / "database.db")

    with sqlite3.connect(cwd / "database.db") as dbconn:
        cursor = dbconn.cursor()

        def include_movie(movie):
            try:
                cursor.execute("INSERT INTO movies_unjoined(title, rating, sequel) VALUES (?, ?, NULL);",
                               [entry_title(movie), movie["vote_average"]])
                movie["dbid"] = cursor.lastrowid
            except Exception as e:
                print("FAIL : ")
                print(movie)
                raise e

        def set_movie_as_sequel(old_movie_id, sequel_movie_id):
            try:
                cursor.execute("UPDATE movies_unjoined SET sequel=? WHERE id=?", [
                               sequel_movie_id, old_movie_id])
            except Exception as e:
                print("FAIL : ", e)
                raise e

        print("Creating database table")
        cursor.execute("""create table `movies_unjoined` (
              `id` integer not null primary key autoincrement,
              `title` varchar(255) not null default "" UNIQUE,
              `rating` FLOAT not null,
              `sequel` INTEGER null,
              FOREIGN KEY(sequel) REFERENCES movies(id)
            );
            """)

        print("Filling data")
        for key, movies in collections.items():
            if key is None:
                for movie in movies:
                    include_movie(movie)

            else:
                if len(movies) == 0:
                    raise Exception("empty collection")
                if len(movies) == 1:
                    include_movie(movies[0])
                else:
                    sorted_movies = sorted(
                        movies, key=lambda a: a["release_date"])

                    # Insert first one
                    first_id = include_movie(sorted_movies[0])

                    # Insert the rest, make references work to the next one.
                    for prequel_movie, sequel_movie in zip(sorted_movies, sorted_movies[1:]):
                        include_movie(sequel_movie)
                        set_movie_as_sequel(
                            prequel_movie["dbid"], sequel_movie["dbid"])
        dbconn.commit()


def add_flag():
    print("Adding a flag")
    with sqlite3.connect(cwd / "database.db") as dbconn:
        cursor = dbconn.cursor()
        cursor.execute(
            "CREATE TABLE flag (`id` integer not null primary key autoincrement, `flag` VARCHAR NOT NULL);")
        cursor.execute(
            "INSERT INTO flag(flag) VALUES (?);", [
                "uhctf{everyone-always-talks-about-the-sql-but-never-about-the-preql-3f85ec}"]
        )


def add_index():
    """Add caching for faster query times"""
    with sqlite3.connect(cwd / "database.db") as dbconn:
        cursor = dbconn.cursor()
        cursor.execute("""CREATE VIEW movies AS 
	            SELECT LOWER(left.title) AS lower_title, left.title, left.rating, right.title AS sequel_title, right.rating AS sequel_rating
                FROM movies_unjoined AS left LEFT OUTER JOIN movies_unjoined AS right on left.sequel=right.id""")


if __name__ == "__main__":
    extract_archive()
    collections = create_collections()
    build_database(collections)
    add_flag()
    add_index()
