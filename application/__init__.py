from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import uuid

app = Flask(__name__)

#setup mysql ENV path in your terminal e.g. mysql+pymysql://user:password@host/name OR sqlite:///databasemane.db
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #supress memory warning when running app
app.config['SECRET_KEY'] = str(uuid.uuid4()) #randomly generated secret key

db = SQLAlchemy(app)

from application import festival_routes
from application import settime_routes