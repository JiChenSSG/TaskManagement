from ..model import Task, engine
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
