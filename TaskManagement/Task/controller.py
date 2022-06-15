from ..model import Task, engine, TaskDetail
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text


def add(task):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(task)
    session.commit()
    id = task.id
    session.close()
    return id


def delete(id):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Task).filter(Task.id == id).update({"status": 0})
    session.commit()
    session.close()
    return 1


def get(name, pageNum, pageSize, order, desc):
    Session = sessionmaker(bind=engine)
    session = Session()
    if desc:
        order = '-' + str(order)

    if name is '':
        tasks = session.query(Task).filter(Task.status == 1).order_by(text(order)).offset(
            pageNum * pageSize).limit(pageSize).all()
    else:
        tasks = session.query(Task).filter(Task.name.like(
            '%' + name + '%'), Task.status == 1).order_by(text(order)).offset(pageNum * pageSize).limit(pageSize).all()
    session.close()
    return tasks


def getScore(id):
    Session = sessionmaker(bind=engine)
    session = Session()

    taskDetail = session.query(TaskDetail).filter(
        TaskDetail.taskId == id).all()

    session.close()
    return taskDetail


def getById(id):
    Session = sessionmaker(bind=engine)
    session = Session()
    task = session.query(Task).filter(Task.id == id).first()
    session.close()
    return task


def getAllNameAndId():
    Session = sessionmaker(bind=engine)
    session = Session()
    tasks = session.query(Task).filter(Task.status == 1).all()
    session.close()
    return tasks
