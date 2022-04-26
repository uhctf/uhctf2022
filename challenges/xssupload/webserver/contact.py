from flask import Blueprint, render_template
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError

blueprint = Blueprint('contact', __name__)

def frodo_required(form, field):
    if "Frodo" not in field.data:
        raise ValidationError("How can you talk about LOTR without mentioning 'Frodo'?")


class ContactForm(FlaskForm):
    full_name = TextAreaField('Full legal name')
    message = TextAreaField('Message for the administrator')
    lotr = TextAreaField('If you had things your way, how would The Lord of the rings end?', validators=[DataRequired(), Length(min=20, max=3000), frodo_required])
    shoesize = SelectField('What shoesize do you have?', validators=[DataRequired()], choices=["30","31","32","33","34","35","36", "37", "38", "39", "40", "41","42","43", "44", "45", "46", "47" ])
    weekday = SelectField('If you could be an animal for one day, which day would you choose?', validators=[DataRequired()], choices=["Monday", "Tuesday", "Wednesday", "Thirsday", "Friday", "Saturday", "Sunday"])
    submit= SubmitField('Send contact form')
    
@blueprint.route("/contact", methods=['get', 'post'])
def contact_put():
    form = ContactForm()
    if form.validate_on_submit():
        return render_template('contact_done.html')
    return render_template('contact.html', form=form)
