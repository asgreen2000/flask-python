
# create a flask blueprint for users route
from flask import Blueprint

users = Blueprint('users', __name__)

from . import auth
from . import info


