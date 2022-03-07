from flask import Flask, render_template, request, url_for #html templates for routes, url_for crud index hyperlinks
from application import app, db
from application.models import Festivals
# from application.forms import CreateForm, UpdateForm #possibly sprint 2?

@app.route('/')
@app.route('/home')
def home():
    return 'My Festival Planner'

@app.route('/create') #CREATE a festival
def create():
    new_festival = Festivals(name ="")
    db.session.add(new_festival)
    db.session.commit()
    return 'Festival created.'

@app.route('/viewall') #READ functionality
def viewall():
    all_festivals = Festivals.query.all()
    festival_string = ""
    for festivals in all_festivals:
        festival_string += "<br>"+ festivals.name
    return festival_string

@app.route('/update/<name>') #UPDATE
def update(name):
    update_festival = Festivals.query.first()
    update_festival.name = name
    db.session.commit()
    return update_festival.name

@app.route('/update/<start_date>') #UPDATE 
def update(start_date):
    update_task = Festivals.query.first()
    update_task.title = title
    db.session.commit()
    return update_task.title

@app.route('/update/<title>') #update task's title after creating it
def update(title):
    update_task = Tasks.query.first()
    update_task.title = title
    db.session.commit()
    return update_task.title
