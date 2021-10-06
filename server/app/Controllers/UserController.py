from flask import request, jsonify
import sqlalchemy
from werkzeug.security import generate_password_hash, check_password_hash
from Models.User import User
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, logout_user, login_required
from flask_jwt_extended import get_jwt_identity, create_access_token, jwt_required
from flask_cors import cross_origin
from server.app.validators.validation import *
from cerberus import Validator
db = SQLAlchemy()


def login_post():
    reqData = request.get_json()
    login_schema = {'require_all': True}
    reqData = request.get_json()
    validated = Validator(login_schema).validate(reqData)
    if validated:
        email = reqData.get("email", None)
        password = reqData.get("password", None)
    else:
        return jsonify({ "msg": "Please fill out the fields!" })

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({ 'msg' : 'Invalid Credentials' })

    login_user(user, remember=True)

    return jsonify({ "msg": "Logged in!" })

def signup_post():
    signup_schema = {'require_all': True,
        'email':{'type':'string', 'check_with': check_email},
        'name':{'type':'string'},
        'universityId':{'type':'string'},
        }
    reqData = request.get_json()
    validator = Validator(signup_schema)
    validated = validator.validate(reqData)
    if validated:
        email = reqData.get("email", None)
        name = reqData.get("name", None)
        password = reqData.get("password", None)
        universityId = reqData.get("universityId", None)
        department = reqData.get("department", None)
        bio = ""
        picture = ""
    else:
        return jsonify({ "msg" : "Invalid data" }), 400
        
    user = User.query.filter_by(email = email).first()
    uid = User.query.filter_by(universityId = universityId).first()

    if user:
        return jsonify ({ "msg": "This email is already existed" }), 400
    if uid : 
        return jsonify ({ "msg": "Use a unique University id" }), 400
    
    newUser = User(email = email, 
                    name = name, 
                    password = generate_password_hash(password, method='sha256'),
                    universityId = universityId, 
                    department = department, 
                    bio = bio,
                    picture = picture,
                    rank = -1,
                    points = 0
                  )

    db.session.add(newUser)
    db.session.commit()
    
    login_user(newUser, remember=True)

    return jsonify({ "msg" : "user created!!" }), 201


@login_required
def logout():
    logout_user()
    return jsonify({ "msg": "logout" })
