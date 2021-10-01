from flask import request, jsonify
import sqlalchemy
from werkzeug.security import generate_password_hash, check_password_hash
from Models.User import User
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def signup_post () :
    reqData = request.get_json()

    email = reqData["email"]
    name = reqData["name"]
    password = reqData["password"]
    universityId = reqData["universityId"]
    department = reqData["department"]
    bio = ""
    picture = ""

    if (email == None or name == None or password == None or universityId == None or department == None) :
        return jsonify({ "msg" : "Invalid data!" }), 400
    # print (email, name, password)

    user = User.query.filter_by(email = email).first()

    if user :
        return jsonify ({ "msg": "user already existed" }), 400
    
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

    return jsonify({ "msg" : "user created!!" }), 201




