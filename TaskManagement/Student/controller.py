import string

from flask import session
from ..model import Task, engine, Student, TaskDetail
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text


def add(student):
    id = 0
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(student)
    session.commit()

    id = student.id
    session.close()

    return id


def get(name, pageNum, pageSize, order, desc):
    Session = sessionmaker(bind=engine)
    session = Session()

    if(desc):
        order = '-' + str(order)

    if(name != ''):
        stu = session.query(Student).filter(Student.name.like(
            '%' + name + '%'), Student.status == 1).order_by(text(order)).offset(pageNum * pageSize).limit(pageSize).all()
    else:
        stu = session.query(Student).filter(Student.status == 1).order_by(text(order)).offset(
            pageNum * pageSize).limit(pageSize).all()

    session.close()

    return stu


def change(student):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Student).filter(Student.id == student.id).update({
        Student.name: student.name,
        Student.age: student.age,
        Student.sex: student.sex,
        Student.grade: student.grade,
        Student.city: student.city
    })

    session.commit()
    session.close()

    return 1


def delete(id):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Student).filter(Student.id == id).update({
        Student.status: 0
    })

    session.commit()
    session.close()

    return 1


def getScore(id):
    Session = sessionmaker(bind=engine)
    session = Session()

    taskDetail = session.query(TaskDetail).filter(
        TaskDetail.studentId == id).all()

    session.close()

    return taskDetail


def getById(id):
    Session = sessionmaker(bind=engine)
    session = Session()

    stu = session.query(Student).filter(Student.id == id).first()

    session.close()

    return stu


def addScore(taskDetail):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(taskDetail)
    session.commit()
    id = taskDetail.id
    session.close()
    return id
