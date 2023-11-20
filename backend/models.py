from . import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    first_name = db.Column(db.String(1000))
    last_name = db.Column(db.String(1000))

class Property(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(1000))
    owner_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class LeaseAgreement(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    owner_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    tenant_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    start_time = db.Column(db.DateTime(timezone=True), nullable=False)
    end_time = db.Column(db.DateTime(timezone=True), nullable=False)
    # Active, Upcoming, Completed, Cancelled status of a lease agreement.
    status  = db.Column(db.Integer, nullable=False)

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    receiver_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    sender_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    payment_date = db.Column(db.DateTime(timezone=True), nullable=False)

class RentalPaymentRecord(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    # Enum representing various states like requested, approved.
    status = db.Column(db.Integer)
    payment_id = db.Column(db.Integer, db.ForeignKey('payment.id'))
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'))
    rental_start_date = db.Column(db.DateTime(timezone=True), nullable=False)
    rental_end_date = db.Column(db.DateTime(timezone=True), nullable=False)
