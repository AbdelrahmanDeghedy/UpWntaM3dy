import sys
from flask import request, jsonify

from Models.Question import Question
from Models.Answer import Answer
from Models.User import User
from flask_sqlalchemy import SQLAlchemy

from flask_login import login_required, current_user



db = SQLAlchemy()

@login_required
def create_answer(qid):
    reqData = request.get_json()
    body = reqData.get("body", None)

    question = Question.query.filter_by(id = qid).first()
    print (question)

    newAnswer = Answer(
                body = body,
                parentQuestion = question,
                owner = current_user
            )

    db.session.close_all()
    db.session.add(newAnswer)
    db.session.commit()
    
    return { 
        'msg' : 'success',
        'answer': newAnswer.serializeAnswer()
     }
