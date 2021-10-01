
from flask import Blueprint

from Controllers.UserController import signup_post, logout, login_post

user_bp = Blueprint('user_bp',__name__)


from flask_login import LoginManager
from flask import jsonify
from Models.User import User





user_bp.route('/signup', methods=['POST'])(signup_post)
user_bp.route('/login', methods=['POST'])(login_post)
user_bp.route('/logout', methods=['GET'])(logout)
