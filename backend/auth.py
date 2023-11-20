from flask import Blueprint, redirect, url_for, request
from . import db
from hashlib import sha1
from flask_login import login_user
from .models import User


auth = Blueprint('auth', __name__)

def generate_password_hash(password):
    print(password)
    print(sha1(password.encode("utf-8")).hexdigest())
    return sha1(password.encode("utf-8")).hexdigest()

def check_password(password, hashed_password):
    print(password)
    print(hashed_password)
    print(generate_password_hash(password))
    return generate_password_hash(password) == hashed_password

@auth.route('/login', methods = ['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    print("hashing: " + password)

    user = User.query.filter_by(email=email).first()
    print(user)
    if user and check_password(password, user.password):
        login_user(user, remember=True)
        return 'Ok', 200
    return 'Failed', 401

@auth.route('/signup', methods = ['POST'])
def signup():
    email = request.form.get('email')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    password = request.form.get('password')
    user = User.query.filter_by(email=email).first()

    if user:
        return "Ok", 403

    new_user = User(email=email, first_name=first_name, last_name=last_name, password=generate_password_hash(password))

    db.session.add(new_user)
    db.session.commit()

    return "Ok", 201

@auth.route('/logout')
def logout():
    return 'Logout'
