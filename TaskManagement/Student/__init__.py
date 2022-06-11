from flask import Blueprint

studentBP = Blueprint('studentBP', __name__)

from . import views