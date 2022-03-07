from application import db
from application.models import Festivals, Set_Times

db.drop_all()
db.create_all()