# compose_flask/app.py
from os import getenv
from flask import Flask, render_template
from redis import Redis
from flask_bootstrap import Bootstrap5

from bspages import blueprint as bspages
from uploadfiles import blueprint as uploadfiles
from uploadfiles_2 import blueprint as uploadfiles_2
from getfiles import blueprint as getfiles
from dmca_request import blueprint as dmca_request
from contact import blueprint as contact


FOOTER_LINKS = [('Home', '/'), ('Terms of Use', '/tos'),
                ('Contact', '/contact'), ('DMCA', '/dmca')]

application = Flask(__name__)
application.config["SECRET_KEY"] = getenv("SECRETKEY")
redis = Redis(host='redis', port=6379)

Bootstrap5(application)
application.register_blueprint(bspages)
application.register_blueprint(getfiles)
application.register_blueprint(dmca_request)
application.register_blueprint(contact)

if getenv("LEVEL") == "0":
    application.register_blueprint(uploadfiles)
if getenv("LEVEL") == "1":
    application.register_blueprint(uploadfiles_2)


@application.route('/')
def hello():
    return 'This Compose/Flask LEVEL {} demo has been viewed {} time(s).'.format(getenv("LEVEL"), redis.get('hits'))


@application.errorhandler(404)
def _(e):
    return render_template('404.html'), 404


@application.errorhandler(500)
def _(e):
    return render_template('500.html'), 500


@application.context_processor
def _inject():
    return dict(footer=FOOTER_LINKS)
