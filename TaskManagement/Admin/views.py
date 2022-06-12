from TaskManagement.model import Admin
from . import adminBP
from flask import jsonify, request
import TaskManagement.Admin.controller as controller


@adminBP.route('/login', methods=['POST'])
def login():
    code = 400
    msg = ''
    data = {}

    username = request.json.get('username')
    password = request.json.get('password')

    if(username and password):
        admin = Admin(username, password, 1)
        id = controller.login(admin)
        if(id != 0):
            msg = 'Login Success'
            data = {'id': id}
            code = 200
        else:
            msg = 'Login Failed'

    return jsonify({'code': code, 'msg': msg, 'data': data})


@adminBP.route('/add', methods=['POST'])
def add():
    code = 400
    msg = ''
    data = {}

    username = request.json.get('username')
    password = request.json.get('password')

    if(username and password):
        admin = Admin(username, password, 1)
        id = controller.add(admin)
        if(id != 0):
            msg = 'Add Success'
            data = {'id': id}
            code = 200
        else:
            msg = 'Add Failed'

    return jsonify({'code': code, 'msg': msg, 'data': data})


@adminBP.route('/get', methods=['POST'])
def get():
    code = 400
    msg = ''
    data = {}

    username = request.json.get('username')
    pageNum = request.json.get('pageNum')
    pageSize = request.json.get('pageSize')

    adminList = controller.get(username, pageNum, pageSize)
    if(adminList):
        msg = 'Get Success'
        for i in adminList:
            data[i.id] = {'username': i.username,
                          'password': i.password, 'status': i.status}

        code = 200
    else:
        msg = 'Get Failed'

    return jsonify({'code': code, 'msg': msg, 'data': data})

@adminBP.route('/change', methods=['POST'])
def change():
    code = 400
    msg = ''
    data = {}

    id = request.json.get('id')
    username = request.json.get('username')
    password = request.json.get('password')
    status = request.json.get('status')

    if(id and username and password and status):
        admin = Admin(username, password, status)
        admin.id = id
        controller.change(admin)
        msg = 'Change Success'
        code = 200

    return jsonify({'code': code, 'msg': msg, 'data': data})

@adminBP.route('/delete', methods=['POST'])
def delete():
    code = 400
    msg = ''
    data = {}

    id = request.json.get('id')
    
    if(id):
        controller.delete(id)
        msg = 'Delete Success'
        code = 200

    return jsonify({'code': code, 'msg': msg, 'data': data})