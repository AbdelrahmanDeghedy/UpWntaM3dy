import sys
from flask import request, jsonify

from Models.Question import Question
from flask_sqlalchemy import SQLAlchemy

from flask_login import login_user, logout_user, login_required, current_user

db = SQLAlchemy()

@login_required
def questions_get():
    questions = Question.query().filter().all()
    return { 
        'msg' : 'success',
        'questions': questions
     }

@login_required
def questions_post() :
    reqData = request.get_json()
    title = reqData.get("title", None)
    body = reqData.get("body", None)
    owner_id = current_user.id

    return {
        'title': title,
        'body': body,
        # 'owner_id': owner_id
    }