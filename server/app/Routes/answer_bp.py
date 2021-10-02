from flask import Blueprint

from Controllers.answerController import create_answer, get_answers, edit_answer, delete_answer, like_answer, dislike_answer, bookmark_answer, removeBookmark_answer

answer_bp = Blueprint('answer_bp',__name__)

answer_bp.route('/<qid>/create', methods=['POST'])(create_answer)
answer_bp.route('/<qid>/', methods=['GET'])(get_answers)
answer_bp.route('/<aid>/edit', methods=['PUT'])(edit_answer)
answer_bp.route('/<aid>/delete', methods=['DELETE'])(delete_answer)
answer_bp.route('/<aid>/like', methods=['POST'])(like_answer)
answer_bp.route('/<aid>/dislike', methods=['POST'])(dislike_answer)
answer_bp.route('/<aid>/bookmark', methods=['POST'])(bookmark_answer)
answer_bp.route('/<aid>/removeBookmark', methods=['POST'])(removeBookmark_answer)
