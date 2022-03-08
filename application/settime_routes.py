from application import app, db
from application.models import Set_Times
from application.forms import CreateForm, UpdateForm

#CRUD for Set_Times table schema below

@app.route('/create_set') #CREATE a set for a given festival
def create_set():
    new_set_time = Set_Times(set_time="", act_name="")
    db.session.add(new_set_time)
    db.session.commit()
    return 'Set time created.'

@app.route('/update/<set_time>') #UPDATE
def update(set_time):
    update_set_time = Set_Times.query.first() #change queries to retrive any record in db
    update_set_time.set_time = set_time
    db.session.commit()
    return update_set_time.set_time

@app.route('/update/<act_name>') #UPDATE
def update(act_name):
    update_set_time = Set_Times.query.first() #change queries to retrive any record in db
    update_set_time.set_time = set_time
    db.session.commit()
    return update_set_time.set_time