from flask import Blueprint

from Controllers.QuestionController import questions_get, questions_post

question_bp = Blueprint('question_bp',__name__)

question_bp.route('/', methods=['Get'])(questions_get)
question_bp.route('/create', methods=['POST'])(questions_post)