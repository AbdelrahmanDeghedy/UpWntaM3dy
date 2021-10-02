import sys
from flask import request, jsonify

from Models.Question import Question
from Models.User import User
from Models.QuestionLikes import QuestionLike
from Models.QuestionBookmarks import QuestionBookmark

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
    department = reqData.get("department", None)
    commaSeparatedTags = reqData.get("commaSeparatedTags", None)


    newQuestion = Question(
                    title = title,
                    body = body,
                    department = department,
                    commaSeparatedTags = commaSeparatedTags,
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

def find_question_by_id (qid) :
    return Question.query.filter_by(id = qid).first()

@login_required
def questions_edit (qid) :
    reqData = request.get_json()
    title = reqData.get("title", None)
    body = reqData.get("body", None)
    department = reqData.get("department", None)
    commaSeparatedTags = reqData.get("commaSeparatedTags", None)


    editedQuestion = Question.query.filter_by(id = qid).first()
    db.session.close_all()

    print (type(editedQuestion.title), type(title))

    editedQuestion.title = title if title != None else find_question_by_id(qid).title
    editedQuestion.body = body if body != None else find_question_by_id(qid).body
    editedQuestion.department = department if department != None else find_question_by_id(qid).department
    editedQuestion.commaSeparatedTags = commaSeparatedTags if commaSeparatedTags != None else find_question_by_id(qid).commaSeparatedTags
    
    
    db.session.add(editedQuestion)
    db.session.commit()

    
    return {
        "msg": "success",
        "Updated Question": editedQuestion.serializeQuestion()
    }

@login_required
def questions_delete (qid) :
    deletedQuestion = Question.query.filter_by(id = qid).first()
    
    
    db.session.close_all()
    db.session.delete(deletedQuestion)
    db.session.commit()

    
    return {
        "msg": "success",
    }

@login_required
def questions_like (qid) :
    if QuestionLike.query.filter_by(likedQid = qid).first() :
        return { 'msg' : 'already liked!' }
    likedQuestion = QuestionLike(
                            likedQid = qid,
                            owner = current_user
                        )
    db.session.close_all()
    db.session.add(likedQuestion)
    db.session.commit()

    return { 
            'msg' : 'success',
            'likedQuestions' : likedQuestion.serializeLike()
           }

@login_required
def questions_dislike (qid) :
    if not (QuestionLike.query.filter_by(likedQid = qid).first()) :
        return { 'msg' : 'already disliked!' }

    likedQues = QuestionLike.query.filter_by(likedQid = qid).first()
    
    db.session.close_all()
    db.session.delete(likedQues)
    db.session.commit()

    return { 
            'msg' : 'success',
           }

@login_required
def questions_bookmark (qid) :
    if QuestionBookmark.query.filter_by(bookmarkedQid = qid).first() :
        return { 'msg' : 'already bookmarked!' }
    bookmarkedQuestion = QuestionBookmark(
                            bookmarkedQid = qid,
                            owner = current_user
                        )
    db.session.close_all()
    db.session.add(bookmarkedQuestion)
    db.session.commit()

    return { 
            'msg' : 'success',
            'likedQuestions' : bookmarkedQuestion.serializeQuestionBookmark()
           }

@login_required
def questions_removeBookmark (qid) :
    if not (QuestionBookmark.query.filter_by(bookmarkedQid = qid).first()) :
        return { 'msg' : 'already not bookmarked!' }

    bookmarkedQuestion = QuestionBookmark.query.filter_by(bookmarkedQid = qid).first()
    
    db.session.close_all()
    db.session.delete(bookmarkedQuestion)
    db.session.commit()

    return { 
            'msg' : 'success',
           }