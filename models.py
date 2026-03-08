from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Violation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_no = db.Column(db.String(20), nullable=False)
    violation_type = db.Column(db.String(100))
    location = db.Column(db.String(100))
    date = db.Column(db.String(20))
    fine_amount = db.Column(db.Integer)
    status = db.Column(db.String(10), default="Unpaid")
