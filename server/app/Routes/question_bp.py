from flask import Blueprint

from Controllers.QuestionController import *

question_bp = Blueprint('question_bp',__name__)

question_bp.route('/', methods=['Get'])(questions_get)  # Sorted by date
question_bp.route('/', methods=['OPTIONS'])(optionsHanlder)
question_bp.route('/sortedByLikes', methods=['GET'])(sort_by_likes)
question_bp.route('/sortedByAnswersCount', methods=['GET'])(sort_by_answersCount)
question_bp.route('/tags', methods=['GET'])(get_tags)
question_bp.route('/create', methods=['POST'])(questions_post)
question_bp.route('<qid>/edit', methods=['PUT'])(questions_edit)
question_bp.route('<qid>/delete', methods=['DELETE'])(questions_delete)
question_bp.route('/<qid>/like', methods=['POST'])(questions_like)
# question_bp.route('/<qid>/total-likes', methods=['GET'])(question_total_likes)
# question_bp.route('/<qid>/is-liked', methods=['GET'])(is_liked_by)
question_bp.route('/<qid>/dislike', methods=['POST'])(questions_dislike)
question_bp.route('/<qid>/bookmark', methods=['POST'])(questions_bookmark)
question_bp.route('/<qid>/removeBookmark', methods=['POST'])(questions_removeBookmark)
