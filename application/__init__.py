from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import getenv
import uuid

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI') #set-up mysql ENV path mysql+pymysql://root:password@host/name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = str(uuid.uuid4()) #randomly generated secret key

db = SQLAlchemy(app)

from application import routes