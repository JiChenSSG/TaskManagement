from TaskManagement.model import Student, TaskDetail
from . import studentBP
from flask import jsonify, request
import TaskManagement.Student.controller as controller
import TaskManagement.Task.controller as taskController


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


@studentBP.route('/getScore', methods=['POST'])
def getScore():
    code = 400
    msg = ''
    data = []

    id = request.json.get('id')

    stu = controller.getScore(id)

    if(stu):
        code = 200
        msg = 'Get Success'
        for i in stu:
            task = taskController.getById(i.taskId)
            data.append({
                'id': i.id,
                'taskName': task.name,
                'score': i.score,
                'taskId': i.taskId
            })
    else:
        msg = 'Get Failed'

    return jsonify({'code': code, 'msg': msg, 'data': data})


@studentBP.route('/addScore', methods=['POST'])
def addScore():
    code = 400
    msg = ''
    data = {}

    studentId = request.json.get('studentId')
    taskId = request.json.get('taskId')
    score = request.json.get('score')

    taskDetail = TaskDetail(taskId, studentId, score, 1)

    if(controller.addScore(taskDetail) != 0):
        msg = 'Add Success'
        code = 200
    else:
        msg = 'Add Failed'

    return jsonify({'code': code, 'msg': msg, 'data': data})


@studentBP.route('/changeScore', methods=['POST'])
def changeScore():
    code = 400
    msg = ''
    data = {}

    id = request.json.get('id')
    studentId = request.json.get('studentId')
    taskId = request.json.get('taskId')
    score = request.json.get('score')
    status = 1

    taskDetail = TaskDetail(taskId, studentId, score, status)
    taskDetail.id = id

    if(controller.changeScore(taskDetail) != 0):
        msg = 'Change Success'
        code = 200
    else:
        msg = 'Change Failed'

    return jsonify({'code': code, 'msg': msg, 'data': data})
