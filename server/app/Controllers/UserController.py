from flask import request, jsonify
import sqlalchemy
from werkzeug.security import generate_password_hash, check_password_hash
from Models.User import User
from flask_sqlalchemy import SQLAlchemy
<<<<<<< Updated upstream
from flask_login import login_user, logout_user, login_required
=======
from flask_jwt_extended import get_jwt_identity, create_access_token, jwt_required
from flask_cors import cross_origin
>>>>>>> Stashed changes

from server.app.validators.validation import *

db = SQLAlchemy()


def login_post():
    reqData = request.get_json()

    email = reqData.get("email", None)
    password = reqData.get("password", None)

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({ 'msg' : 'Invalid Credentials' })

    login_user(user, remember=True)

    return jsonify({ "msg": "Logged in!" })

def signup_post():
    signup_schema = {'require_all': True,
        'email':{'type':'string', 'check_with': check_email},
        'name':{'type':'string'},
        'password':{'type':'str'}
    }
    reqData = request.get_json()

    email = reqData.get("email", None)
    name = reqData.get("name", None)
    password = reqData.get("password", None)
    universityId = reqData.get("universityId", None)
    department = reqData.get("department", None)
    bio = ""
    picture = ""

    #To be modified....
    if (email == None or name == None or password == None or universityId == None or department == None) :
        return jsonify({ "msg" : "Invalid data" }), 400

    # print (email, name, password, universityId, department)

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
