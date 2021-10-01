from flask import Flask
from app.controllers.auth.authController import *
from flask_sqlalchemy import SQLAlchemy


# def createApp() :

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisismysecretkeydonotstealit'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///home/deghedy/Desktop/UpWntaM3dy/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db = SQLAlchemy(app)


    # return app