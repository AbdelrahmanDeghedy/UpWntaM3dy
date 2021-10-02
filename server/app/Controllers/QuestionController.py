import sys
from flask import request, jsonify

from Models.Question import Question
from Models.User import User
from flask_sqlalchemy import SQLAlchemy

from flask_login import login_required, current_user



db = SQLAlchemy()

@login_required
def questions_get():
    questions = Question.query.filter().all()
    questionsList = [question.serializeQuestion() for question in questions]
    
    return { 
        'msg' : 'success',
        'length' : len(questionsList),
        'questions': questionsList
     }

@login_required
def questions_post() :
    reqData = request.get_json()
    title = reqData.get("title", None)
    body = reqData.get("body", None)


    newQuestion = Question(
                    title = title,
                    body = body,
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

@login_required
def questions_bookmark () :
    # bookmarks = [bookmark.id for bookmark in list(self.bookmarks)]
    user = User.query.filter().first()
    print (type(user), user)
    user.bookmarks = [list(user.bookmarks), "test"]
    print (user.serializeUser())
    # db.session.commit()
    # print (current_user.serializeUser())
    return { 'msg' : 'success' }