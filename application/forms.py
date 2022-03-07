from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, DateTimeField
from wtforms.validators import DataRequired, Length, ValidationError

class CreateForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2,max=50)])
    start_date = DateTimeField('Start Date', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired(), Length(min=2,max=300)])
    submit = SubmitField('Create')

class UpdateForm(FlaskForm):
    name = StringField('Title', validators=[DataRequired(), Length(min=2,max=30)])
    set_time = DateTimeField('Description', validators=[DataRequired(), Length(min=2,max=300)])
    attended = BooleanField('Attended')
    submit = SubmitField('Update')