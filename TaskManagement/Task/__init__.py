from flask import Blueprint

taskBP = Blueprint('taskBP', __name__)

from . import views