import sys
from flask import request, jsonify

from Models.Question import Question
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def index():
    return "This is report controller!"