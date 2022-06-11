from flask import Blueprint

teacherBP = Blueprint('teacherBP', __name__)

from . import views