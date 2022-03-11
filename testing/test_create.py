from flask import url_for
from flask_testing import TestCase
from os import getenv
import uuid

from application import app, db, Festivals, Set_Times

# base class for test creation
class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('DATABASE_URI'), #test sqlite
        SECRET_KEY=str(uuid.uuid4()), #randomly generated secret key,
        debug=True,
        WTF_CSRF_ENABLED=False, #in production set to true
        )
        return app

# Called before every test
    def setUp(self):
        db.create_all()
        sample1 = Festivals(name="Test Fest")
        db.session.add(sample1)
        db.session.commit()

# Called after every test
    def tearDown(self):
        # Close the database session and remove all contents of the database
        db.session.remove()
        db.drop_all()

# Test class
class TestViews(TestBase):
    def test_index_get(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Fest', response.data)