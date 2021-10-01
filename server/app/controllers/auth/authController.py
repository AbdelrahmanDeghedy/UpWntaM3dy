from flask import request, jsonify, redirect, url_for, flash, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from models.auth.authModels import User
from app.models.auth.authModels import db
from flask_login import login_user, logout_user, login_required


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
def login_post():
    reqData = request.get_json()

    email = reqData.get("email", None)
    password = reqData.get("password", None)

    user = User.query.filter_by(email=email).first()

    if not user and not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('login_post'))

    login_user(user, remember=True)

    return jsonify({ "msg": "Logged in!" })

@auth.route('/signup', methods=['POST'])
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

    print (email, name, password, universityId, department)

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

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({ "msg": "logout" })


