from flask import Blueprint, render_template, Response
import storage

blueprint = Blueprint('getfiles', __name__)


@blueprint.get("/file/<file_id>")
def get_file(file_id):
    value = storage.lookup_item(file_id)
    if value is None:
        return render_template("404.html"), 404
    response = Response(value)
    return response
