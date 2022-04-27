from flask import Blueprint, render_template, request
from flask_wtf.file import FileRequired, FileSize
from flask_wtf import FlaskForm
from wtforms.fields import FileField
from wtforms.validators import ValidationError
from os import getenv
from os.path import splitext

import storage

blueprint = Blueprint('uploadfiles', __name__)

BLOCKED = [b'script', b'fetch', b'xmlhttprequest']


def file_does_not_contain_blocked_words(_, field):
    file = field.data.read().lower()
    field.data.seek(0)
    for word in BLOCKED:
        if word in file:
            raise ValidationError("Your file contains a forbidden word")


def file_extension(_, field):
    filename = field.data.filename
    extension = splitext(filename)[1].strip(".")
    if extension == "HTML":
        raise ValidationError("This file extension cannot be used")


class FileUploadForm(FlaskForm):
    file = FileField(label="", validators=[FileRequired(), FileSize(
        1024), file_does_not_contain_blocked_words])


@blueprint.route("/", methods=['get', 'post'])
def insert_file():
    uploadform = FileUploadForm()
    if uploadform.validate_on_submit():
        file = uploadform.file.data.read()
        uid = storage.create_item(file)
        return render_template('uploaded.html', uid=uid, domain=getenv("BASEDOMAIN"))
    else:
        return render_template('index.html', form=uploadform)
