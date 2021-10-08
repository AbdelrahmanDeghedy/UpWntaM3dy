
from flask import Blueprint

from Controllers.UserController import *

user_bp = Blueprint('user_bp',__name__)

user_bp.route('/', methods=['OPTIONS'])(optionsHanlder)
user_bp.route('/signup', methods=['POST'])(signup_post)
user_bp.route('/login', methods=['POST'])(login_post)
user_bp.route('/edit', methods=['PUT'])(user_edit)
# user_bp.route('/logout', methods=['GET'])(logout)
user_bp.route('/<uid>/delete', methods=['DELETE'])(user_delete)
user_bp.route('/currentUser', methods=['GET'])(currnetUser)
user_bp.route('/leaderboard', methods=['GET'])(get_leaderboard)

user_bp.route('/<uid>/likes', methods=['GET'])(get_user_likes)


