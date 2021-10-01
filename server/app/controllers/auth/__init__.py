from flask import Blueprint
from flask_login import LoginManager
from flask import jsonify
from app.models.auth.authModels import User

auth = Blueprint('auth', __name__)


login_manager = LoginManager()
login_manager.login_view = 'login_post'
login_manager.init_app(auth)

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

@login_manager.unauthorized_handler
def unauth_handler():
    return jsonify(message='You are not authorized to access this page'), 401
