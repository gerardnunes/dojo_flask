from flask import Blueprint

from app.user.models import User

user_bp = Blueprint('user', __name__)


@user_bp.route('/user', methods=['GET'])
def user():
    return 'Opa'