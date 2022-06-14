import re
from TaskManagement.model import Task
from . import taskBP
from flask import jsonify, request
import TaskManagement.Task.controller as controller


@taskBP.route('/add', methods=['POST'])
def add():
    code = 400
    msg = ''
    data = {}

    name = request.json.get('name')
    date = request.json.get('date')

    status = 1

    task = Task(name, date, status)

    id = controller.add(task)

    if(id != 0):
        code = 200
        msg = 'Add Success'
        data = {"id": id}
    else:
        msg = 'Add Failed'

    return jsonify({'code': code, 'msg': msg, 'data': data})


@taskBP.route('/delete', methods=['POST'])
def delete():
    code = 400
    msg = ''
    data = {}

    id = request.json.get('id')

    id = controller.delete(id)

    if(id != 0):
        code = 200
        msg = 'Delete Success'
        data = {"id": id}
    else:
        msg = 'Delete Failed'

    return jsonify({'code': code, 'msg': msg, 'data': data})


@taskBP.route('/get', methods=['POST'])
def get():
    code = 400
    msg = ''
    data = []

    name = ''
    name = request.json.get('name')
    pageNum = request.json.get('pageNum')
    pageSize = request.json.get('pageSize')
    order = request.json.get('order')
    desc = request.json.get('desc')

    tasks = controller.get(name, pageNum, pageSize, order, desc)



    if(tasks):
        for i in tasks:
            data.append({'id': i.id, 'date': i.date, 'name': i.name})
        code = 200
        msg = 'Get Success'
    else:
        msg = 'Get Failed'

    return jsonify({'code': code, 'msg': msg, 'data': data})
