from flask import url_for
from flask_testing import TestCase
from os import getenv
import uuid

from application import app, db, Festivals, Set_Times

#base class for test creation
class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('DATABASE_URI'), #test sqlite
        SECRET_KEY=str(uuid.uuid4()), #randomly generated secret key,
        debug=True,
        WTF_CSRF_ENABLED=False, #in production set to true
        )
        return app