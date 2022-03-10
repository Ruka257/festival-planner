from flask import Flask, render_template, request, url_for #html templates for routes, url_for crud index hyperlinks
from application import app, db
from datetime import date
from application.models import Festivals
from application.forms import CreateForm, UpdateForm

@app.route('/')
@app.route('/home')
def home():
    return 'My Festival Planner'

@app.route('/viewall') #READ functionality
def viewall():
    all_festivals = Festivals.query.all()
    festival_string = ""
    for festivals in all_festivals:
        festival_string += "<br>"+ festivals.name
    return festival_string

@app.route('/create') #CREATE a festival with all attributes in Festivals table
def create():
    new_festival = Festivals(festival_name="", start_date="", location="")
    db.session.add(new_festival)
    db.session.commit()
    return 'Festival created.'

@app.route('/create/<festival_name>')
def create(festival_name):
    new_festival = Festivals(festival_name=festival_name, description="Describe festival here...")
    db.session.add(new_festival)
    db.session.commit()
    return f'Created new festival: {festival_name}'

@app.route('/update/<name>') #UPDATE
def update(name):
    update_festival = Festivals.query.first()
    update_festival.name = name
    db.session.commit()
    return update_festival.name

@app.route('/update/<start_date>') #UPDATE 
def update(start_date):
    update_festival = Festivals.query.first()
    update_festival.start_date = start_date
    db.session.commit()
    return update_festival.start_date

@app.route('/update/<location>') #UPDATE
def update(location):
    update_festival = Festivals.query.first() #change queries to retrive any record in db
    update_festival.location = location
    db.session.commit()
    return update_festival.location