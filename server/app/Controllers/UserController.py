from flask import request, jsonify
from flask_jwt_extended.utils import get_current_user
import sqlalchemy
from werkzeug.security import generate_password_hash, check_password_hash
from Models.User import User
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, logout_user, login_required
from flask_jwt_extended import get_jwt_identity, create_access_token, jwt_required
from flask_cors import cross_origin
from server.app.validators.validation import *
from cerberus import Validator
from flask_jwt_extended import get_jwt_identity, create_access_token, jwt_required
from flask_cors import cross_origin
db = SQLAlchemy()

@jwt_required()
@cross_origin()
def get_leaderboard () :
        users = User.query.filter().all()
        usersList = [user.serializeUser() for user in users]
        usersList = sorted(usersList, key = lambda k : k['rank'], reverse=True)

        return {
            'msg': 'Success',
            'length' : len(usersList),
            'users': usersList
        }
@cross_origin()
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


    access_token = create_access_token(identity=user.universityId)

    
    return jsonify({
        'msg' : 'success',
        'user' : user.serializeUser(),
        'token': access_token
    })

@cross_origin()
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
                    points = 0,
                  )

    db.session.add(newUser)
    db.session.commit()
    
    access_token = create_access_token(identity=newUser.universityId)

    return jsonify({ 
        'msg' : 'success',
        'user' : newUser.serializeUser(),
        'token': access_token
     }), 201


@jwt_required()
@cross_origin()
def user_edit():
    reqData = request.get_json()

    email = reqData.get("email", None)
    name = reqData.get("name", None)
    password = reqData.get("password", None)
    bio = reqData.get("bio", None)
    picture = reqData.get("picture", None)
    rank = reqData.get("rank", None)
    points = reqData.get("points", None)

    user = User.query.filter_by(universityId = json.loads(getCurrnetUser().data)['universityId']).first()


    db.session.close_all()

    user.email = email if email != None and not (User.query.filter_by(email = email).first()) else user.email
    user.password = generate_password_hash(password, method='sha256') if password != None else user.password
    user.name = name if name != None else user.name
    user.bio = bio if bio != None else user.bio
    user.picture = picture if picture != None else user.picture
    user.rank = rank if rank != None else user.rank
    user.points = points if points != None else user.points

    db.session.add(user)
    db.session.commit()
    

    return jsonify({ "msg" : "user updated!!" }), 200

@jwt_required()
@cross_origin()
def user_delete(uid):
    deletedUser = User.query.filter_by(universityId = uid).first()

    db.session.close_all()
    db.session.delete(deletedUser)
    db.session.commit()    

    return jsonify({ "msg" : "user deleted!!" }), 200


# @jwt_required()
# def logout():
#     logout_user()
#     return jsonify({ "msg": "logout" })

@jwt_required()
@cross_origin()
def currnetUser():
    currentUser = get_jwt_identity()
    return { 'currentUserId' : currentUser }, 200

import json

@jwt_required()
@cross_origin()
def getCurrnetUser():
    currentUserId = get_jwt_identity()
    currentUser = User.query.filter_by (universityId = currentUserId).first()
    return json.dumps(currentUser.serializeUser())


@cross_origin()
def optionsHanlder() :
    return "OK", 200