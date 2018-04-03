from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class FieldForm(FlaskForm):
    name = StringField('Field Name', validators=[DataRequired()])
    submit = SubmitField('Create Field')

class FieldValueForm(FlaskForm):
    field = SelectField('Field Name', choices=[])
    value = TextAreaField('Value')
    submit = SubmitField('Create Value')