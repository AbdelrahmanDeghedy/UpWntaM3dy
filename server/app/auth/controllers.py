from flask import Flask
from flask_restful import Resource, Api, reqparse
from models import User
from models import db

parser = reqparse.RequestParser()


app = Flask(__name__)
api = Api(app)

class Signup(Resource):
    def post(self):
        parser.add_argument('email', 'password')
        args = parser.parse_args()
        return args , 201

api.add_resource(Signup, '/api/v1/users/signup')

if __name__ == '__main__':
    app.run(debug=True)



# admin = User (name = "admin", universityId = 18010917, email = "test@test.com", password = "password", points = 0, rank = -1, bio = "", picture = "", department = "communication")

# db.session.add(admin)
# db.session.commit()

