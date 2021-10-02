from flask import request, jsonify
import sqlalchemy
from werkzeug.security import generate_password_hash, check_password_hash
from Models.User import User
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, logout_user, login_required, current_user

db = SQLAlchemy()


def get_leaderboard () :
        users = User.query.filter().all()
        usersList = [user.serializeUser() for user in users]
        usersList = sorted(usersList, key = lambda k : k['rank'], reverse=True)

        return {
            'msg': 'Success',
            'length' : len(usersList),
            'users': usersList
        }

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
    reqData = request.get_json()

    email = reqData.get("email", None)
    name = reqData.get("name", None)
    password = reqData.get("password", None)
    universityId = reqData.get("universityId", None)
    department = reqData.get("department", None)
    bio = ""
    picture = ""

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
                    points = 0,
                  )

    db.session.add(newUser)
    db.session.commit()
    
    login_user(newUser, remember=True)

    return jsonify({ "msg" : "user created!!" }), 201

@login_required
def user_edit():
    reqData = request.get_json()

    email = reqData.get("email", None)
    name = reqData.get("name", None)
    password = reqData.get("password", None)
    bio = reqData.get("bio", None)
    picture = reqData.get("picture", None)
    rank = reqData.get("rank", None)
    points = reqData.get("points", None)

    user = User.query.filter_by(email = current_user.email).first()
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

@login_required
def user_delete():
    deletedUser = User.query.filter_by(id = current_user.id).first()

    db.session.close_all()
    db.session.delete(deletedUser)
    db.session.commit()
    logout_user()
    

    return jsonify({ "msg" : "user deleted!!" }), 200


@login_required
def logout():
    logout_user()
    return jsonify({ "msg": "logout" })

@login_required
def currnetUser():
    return current_user.serializeUser()

