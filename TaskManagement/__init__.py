from flask import Flask

from .Admin import admin
from .Teacher import teacher
from .Student import student


app = Flask(__name__)

app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(teacher, url_prefix='/teacher')
app.register_blueprint(student, url_prefix='/student')
