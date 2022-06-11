from flask import Blueprint

adminBP = Blueprint('adminBP', __name__)

from . import views