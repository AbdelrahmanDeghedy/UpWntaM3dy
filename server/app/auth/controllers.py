from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from models import db, app
from werkzeug.security import safe_str_cmp
# from flask_jwt import JWT, jwt_required, current_identity

# app.config['SECRET_KEY'] = 'super-secret'


# def authenticate(email, password):
#     user = user = User.query.filter_by(email = email).first()
#     if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
#         return user

# def identity(payload):
#     user_id = payload['identity']
#     return User.query.filter_by(id = user_id).first()

# jwt = JWT(app, authenticate, identity)


@app.route("/signup", methods = ["POST"])
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


if __name__ == '__main__':
    app.run(debug=True)



