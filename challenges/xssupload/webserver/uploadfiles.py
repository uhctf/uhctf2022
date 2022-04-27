from distutils.command.upload import upload
from flask import Blueprint, render_template, request
from flask_wtf.file import FileRequired, FileSize
from flask_wtf import FlaskForm
from wtforms.fields import FileField
from os import getenv

import storage

blueprint = Blueprint('uploadfiles', __name__)


class FileUploadForm(FlaskForm):
    file = FileField(label="", validators=[FileRequired(), FileSize(1024)])


@blueprint.route("/", methods=['get', 'post'])
def insert_file():
    uploadform = FileUploadForm()
    if uploadform.validate_on_submit():
        file = uploadform.file.data.read()
        print("file is {}".format(file))
        uid = storage.create_item(file)
        return render_template('uploaded.html', uid=uid, domain=getenv("BASEDOMAIN"))
    else:
        return render_template('index.html', form=uploadform)
