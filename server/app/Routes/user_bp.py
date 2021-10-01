
from flask import Blueprint

from Controllers.UserController import signup_post

user_bp = Blueprint('user_bp',__name__)

user_bp.route('/signup', methods=['POST'])(signup_post)
