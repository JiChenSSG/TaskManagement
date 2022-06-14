from .Student import studentBP
from .Admin import adminBP
from .Task import taskBP
from flask import Blueprint, Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)

CORS(app, supports_credentials=True)

app.register_blueprint(adminBP, url_prefix='/admin')
app.register_blueprint(studentBP, url_prefix='/student')
app.register_blueprint(taskBP, url_prefix='/task')
