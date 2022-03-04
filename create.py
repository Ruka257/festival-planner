from application import db
from application.models import festivals, timeslots

db.drop_all()
db.create_all()