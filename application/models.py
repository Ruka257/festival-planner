from enum import unique
from sqlalchemy import ForeignKey, ForeignKeyConstraint, UniqueConstraint, null
from application import db
from datetime import datetime, date

class Festivals(db.Model): #schema
    festival_id = db.Column(db.Integer, unique=True, primary_key=True)
    festival_name = db.Column(db.__str__(50), nullable=False)
    start_date = db.Column(db.date)
    location = db.Column(db.__str__(100), nullable=False)
    attended = db.Column(db.Boolean, default=False)

class Set_Times(db.Model): #schema
    set_time_id = db.Column(db.Integer, unique=True, primary_key=True)
    set_time = db.Column(db.datetime)
    festival_id = db.Column(db.Integer, unique=True, ForeignKey=True) #FK calling from...?
    act_name = db.Column(db.__str__(100), nullable=False)
    seen = db.Column(db.Boolean, default=False)