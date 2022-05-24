from flask import Blueprint, render_template
from flask_wtf import FlaskForm
from wtforms import EmailField, SubmitField, BooleanField, StringField
from wtforms.validators import DataRequired, Email, UUID, ValidationError


from storage import lookup_item, submit_dmca_request

blueprint = Blueprint('dmca', __name__)


def uuid_exists(_form, field):
    uuid = field.data
    if lookup_item(uuid) is None:
        raise ValidationError("This UUIDv4 doesn't exist")
    return None


class DMCAForm(FlaskForm):
    email = EmailField('Email address', validators=[DataRequired(), Email()])
    uuid = StringField(
        'UUIDv4 of the file', description='We name it this to gatekeep our DMCA requests. It\'s the part after /file/', validators=[UUID(), uuid_exists])
    checkbox0 = BooleanField(
        'I declare that I am the copyright holder of the submitted work.', validators=[DataRequired()])
    checkbox1 = BooleanField(
        "I declare that I did not fill in this form just to have the administrator look at the specified file from their regular browser. I pinky promise that it doesn 't contain anything harmful.", validators=[DataRequired()])
    submit = SubmitField('Submit DMCA query')


@blueprint.route("/dmca", methods=['get', 'post'])
def dmca():
    form = DMCAForm()
    if form.validate_on_submit():
        uuid = form.uuid.data
        submit_dmca_request(uuid)
        return render_template('dmca_complete.html', form=form)

    return render_template('dmca.html', form=form)
