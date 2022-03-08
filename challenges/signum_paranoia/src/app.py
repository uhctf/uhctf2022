import os
from dotenv import load_dotenv
from flask import Flask, request, send_from_directory, current_app, redirect, url_for
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

load_dotenv()
app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=[]
)


@app.route("/assets/<path:path>")
def send_assets(path):
    return send_from_directory("assets", path)


@app.route("/forms/<path:path>")
def send_forms(path):
    return send_from_directory("forms", path)


@app.route('/')
def root():
    return current_app.send_static_file('index.html')


@app.route('/index')
def index():
    return current_app.send_static_file('index.html')


@app.route('/about')
def about():
    return current_app.send_static_file('about.html')


@app.route('/pricing')
def pricing():
    return current_app.send_static_file('pricing.html')


@app.route('/testimonials')
def testimonials():
    return current_app.send_static_file('testimonials.html')


@app.route('/register', methods=['GET'])
def register_get():
    return current_app.send_static_file('register.html')


@app.route('/register', methods=['POST'])
def register_post():
    return 'OK: Registration received!<br>Your registration will undergo rigorous security checks. ETA: 50 working days.'


@app.route('/login', methods=['GET'])
@limiter.limit("4/second", override_defaults=True)
def login_get():
    return current_app.send_static_file('login.html')


@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['name']
    password = request.form['password']

    if username == 'administrator' and password == '@Q$y5b2!':
        return f"OK: {os.getenv('FLAG')}"
    return 'Invalid credentials or the account has not gone through our verification process yet.'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
