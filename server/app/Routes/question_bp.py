from flask import Blueprint

from Controllers.QuestionController import questions_get, questions_post, questions_like, questions_dislike

question_bp = Blueprint('question_bp',__name__)

question_bp.route('/', methods=['Get'])(questions_get)
question_bp.route('/create', methods=['POST'])(questions_post)
question_bp.route('/<qid>/like', methods=['POST'])(questions_like)
question_bp.route('/<qid>/dislike', methods=['POST'])(questions_dislike)
# question_bp.route('<:qid>/like', methods=['POST'])(questions_post)
# increments the likes of qid by 1, and adds it to the user's likes 