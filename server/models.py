from datetime import datetime
from server import db


class TestCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    input = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    time = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
