from flask import Blueprint

from Controllers.answerController import create_answer

answer_bp = Blueprint('answer_bp',__name__)

answer_bp.route('/<qid>/create', methods=['POST'])(create_answer)
