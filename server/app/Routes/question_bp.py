from flask import Blueprint

from Controllers.QuestionController import questions_get, questions_post, questions_like, questions_dislike, questions_bookmark, questions_removeBookmark, questions_edit, questions_delete

question_bp = Blueprint('question_bp',__name__)

question_bp.route('/', methods=['Get'])(questions_get)
question_bp.route('/create', methods=['POST'])(questions_post)
question_bp.route('<qid>/edit', methods=['PUT'])(questions_edit)
question_bp.route('<qid>/delete', methods=['DELETE'])(questions_delete)
question_bp.route('/<qid>/like', methods=['POST'])(questions_like)
question_bp.route('/<qid>/dislike', methods=['POST'])(questions_dislike)
question_bp.route('/<qid>/bookmark', methods=['POST'])(questions_bookmark)
question_bp.route('/<qid>/removeBookmark', methods=['POST'])(questions_removeBookmark)