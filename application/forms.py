from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, DateTimeField
from wtforms.validators import DataRequired, Length, ValidationError

class CreateForm(FlaskForm):
    name = StringField('Title', validators=[DataRequired(), Length(min=2,max=30)])
    location = StringField('Description', validators=[DataRequired(), Length(min=2,max=300)])
    submit = SubmitField('Create')

class UpdateForm(FlaskForm):
    name = StringField('Title', validators=[DataRequired(), Length(min=2,max=30)])
    #timeslot = DateTimeField('Description', validators=[DataRequired(), Length(min=2,max=300)])
    attended = BooleanField('Attended')
    submit = SubmitField('Update')