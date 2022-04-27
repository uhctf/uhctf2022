from flask import Blueprint, render_template

blueprint = Blueprint('bsfiles', __name__)


@blueprint.get("/tos")
def tos():
    return render_template('tos.html')


@blueprint.get("/privacy")
def privacy():
    return render_template('tos.html')
