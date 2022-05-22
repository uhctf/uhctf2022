from crypt import methods
from flask import Blueprint, render_template, request, session

from src.fontprinter import FontSession

PASSWORD = "pa$$\/\/()Rd"
app = Blueprint('page', 'page', static_folder="/static")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if request.form.get("password", "") != PASSWORD:
            return render_template("wrongpassword.html")
        
        fingerprint = session.get("fingerprint")

        if fingerprint is None:
            return render_template("wrong.html")
        if not FontSession(fingerprint).is_good_for_safe():
            return render_template("wrong.html")
        
        return render_template("correct.html")
        
    else:
        return render_template("index.html")
