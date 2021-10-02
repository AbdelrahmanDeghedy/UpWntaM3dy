import sys
from flask import request, jsonify

from Models.Question import Question
from flask_sqlalchemy import SQLAlchemy

from flask_login import login_required, current_user

db = SQLAlchemy()

@login_required
def questions_get():
    questions = Question.query.filter().all()
    questionsList = [question.serializeQuestion() for question in questions]
    
    return { 
        'msg' : 'success',
        'questions': questionsList
     }

@login_required
def questions_post() :
    reqData = request.get_json()
    title = reqData.get("title", None)
    body = reqData.get("body", None)
    owner_id = current_user.id

    print (current_user.id)

    newQuestion = Question(
                    title = title,
                    body = body,
                    owner_id = owner_id,
                    owner = current_user
                )
    print (newQuestion)
    db.session.close_all()
    db.session.add(newQuestion)
    db.session.commit()
    return {
        "msg": "success",
        "Created Question": newQuestion.serializeQuestion()
    }