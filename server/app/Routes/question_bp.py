from flask import Blueprint

from Controllers.QuestionController import index

question_bp = Blueprint('question_bp',__name__)

question_bp.route('/', methods=['Get'])(index)