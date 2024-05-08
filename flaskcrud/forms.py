from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, SelectMultipleField
from wtforms.widgets import CheckboxInput
from wtforms.validators import DataRequired, Email


class PublisherForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    address = StringField('Address')
    city = StringField('City')
    state = StringField('State')
    country = StringField('Country')
    website = StringField('Website')
    submit = SubmitField('Submit')


class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    authors = SelectMultipleField('Authors', coerce=int, option_widget=CheckboxInput())
    publisher_id = SelectField('Publisher', coerce=int, validators=[DataRequired()])
    pub_date = DateField('Publication Date', format='%Y-%m-%d', validators=[DataRequired()])


class AuthorForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')