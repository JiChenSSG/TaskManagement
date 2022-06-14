from TaskManagement.model import Student
from . import studentBP
from flask import jsonify, request
import TaskManagement.Student.controller as controller


@studentBP.route('/add', methods=['POST'])
def add():
    code = 400
    msg = ''
    data = {}

    name = request.json.get('name')
    age = request.json.get('age')
    sex = request.json.get('sex')
    grade = request.json.get('grade')
    city = request.json.get('city')
    status = 1

    stu = Student(name, age, sex, grade, city, status)

    id = controller.add(stu)
    if(id != 0):
        code = 200
        msg = 'Add Success'
        data = {"id": id}
    else:
        msg = 'Add Failed'

    return jsonify({'code': code, 'msg': msg, 'data': data})


@studentBP.route('/get', methods=['POST'])
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

    stu = None

    stu = controller.get(name, pageNum, pageSize, order, desc)

    if(stu):
        code = 200
        msg = 'Get Success'
        for i in stu:
            data.append({
                'id': i.id,
                'name': i.name,
                'age': i.age,
                'sex': i.sex,
                'grade': i.grade,
                'city': i.city
            })
    else:
        msg = 'Get Failed'

    return jsonify({'code': code, 'msg': msg, 'data': data})


@studentBP.route('change', methods=['POST'])
def change():
    code = 400
    msg = ''
    data = {}

    id = request.json.get('id')
    name = request.json.get('name')
    age = request.json.get('age')
    sex = request.json.get('sex')
    grade = request.json.get('grade')
    city = request.json.get('city')
    status = 1

    stu = Student(name, age, sex, grade, city, status)
    stu.id = id

    if(controller.change(stu) == 1):
        msg = 'Change Success'
        code = 200

    return jsonify({'code': code, 'msg': msg, 'data': data})


@studentBP.route('delete', methods=['POST'])
def delete():
    code = 400
    msg = ''
    data = {}

    id = request.json.get('id')

    if(controller.delete(id) == 1):
        msg = 'Delete Success'
        code = 200

    return jsonify({'code': code, 'msg': msg, 'data': data})
