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

@login_required
def get_answers (qid) :
    questionAnswers = Answer.query.filter_by(parentQuestion_id = qid).all()
    questionAnswers = [answer.serializeAnswer() for answer in questionAnswers]

    return {
        'msg' : 'success',
        'length': len(questionAnswers),
        'Answers' : questionAnswers
    }

@login_required
def edit_answer(aid):
    reqData = request.get_json()
    body = reqData.get("body", None)

    editedAnswer = Answer.query.filter_by(id = aid).first()

    editedAnswer.body = body

    db.session.close_all()
    db.session.add(editedAnswer)
    db.session.commit()
    
    return { 
        'msg' : 'success',
        'editedAnswer': editedAnswer.serializeAnswer()
     }

@login_required
def delete_answer(aid):

    deletedAnswer = Answer.query.filter_by(id = aid).first()

    db.session.close_all()
    db.session.delete(deletedAnswer)
    db.session.commit()
    
    return { 
        'msg' : 'success',
     }