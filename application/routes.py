from flask import FLASK, render_template, url_for #htmls templates for routes, url_for crud index hyperlinks
from application import app, db
from application.models import Tasks
# from application.forms import CreateForm, UpdateForm #possibly sprint 2?

@app.route('/')
@app.route('/home')
def home():
    return 'Welcome to the Festival Planner'

@app.route('/viewall')
def viewall():
    all_festivals = Festivals.query.all()
    festival_string = ""
    for festival in all_festivals:
        task_string += "<br>"+ festival.name
    return festival_string