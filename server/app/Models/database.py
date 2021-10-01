from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#Creates db instance
app = Flask(__name__)
db = SQLAlchemy()