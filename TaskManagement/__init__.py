from .Student import studentBP
from .Teacher import teacherBP
from .Admin import adminBP
from flask import Blueprint, Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)

app.register_blueprint(adminBP, url_prefix='/admin')
app.register_blueprint(teacherBP, url_prefix='/teacher')
app.register_blueprint(studentBP, url_prefix='/student')

from . import model