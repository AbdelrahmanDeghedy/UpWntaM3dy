from flask import Flask
from flask_migrate import Migrate
from Models.database import db 

#Each model should be imported here for migrations
from Models.Question import Question
from Models.User import User
from Models.Report import Report
from Models.Answer import Answer

#Import Routes BluePrints
from Routes.question_bp import question_bp
from Routes.answer_bp import answer_bp
from Routes.user_bp import user_bp
from Routes.report_bp import report_bp

import os
# from server.app.models.Question import *


app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(question_bp, url_prefix='/questions')
app.register_blueprint(answer_bp, url_prefix='/answers')
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(report_bp, url_prefix='/reports')

from flask_jwt_extended import JWTManager
jwt = JWTManager(app)

from flask_cors import CORS

CORS(app)

@app.route('/')
def index():
    return 'This is index!'

if __name__ == '__main__':
    app.run(debug=True)
