from .. import model
from TaskManagement.model import engine
from sqlalchemy.orm import sessionmaker


def login(admin):
    Session = sessionmaker(bind=engine)
    session = Session()
    admin = session.query(model.Admin).filter(model.Admin.username ==
                                              admin.username, model.Admin.password == admin.password, model.Admin.status == 1).one_or_none()
    session.close()

    if admin is None:
        return 0
    else:
        return admin.id


def add(admin):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(admin)
    session.commit()

    id = admin.id

    session.close()

    return id


def get(username, pageNum, pageSize):
    Session = sessionmaker(bind=engine)
    session = Session()
    if(username != ''):
        admin = session.query(model.Admin).filter(model.Admin.username.like(
            '%' + username + '%'), model.Admin.status == 1).offset(pageNum * pageSize).limit(pageSize).all()  # 获取分页数据
    else:
        admin = session.query(model.Admin).filter(model.Admin.status == 1).offset(
            pageNum * pageSize).limit(pageSize).all()
    session.close()

    if admin is None:
        return 0
    else:
        return admin


def change(admin):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(model.Admin).filter(model.Admin.id == admin.id).update({
        model.Admin.username: admin.username, model.Admin.password: admin.password, model.Admin.status: admin.status})
    session.commit()
    session.close()


def delete(id):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(model.Admin).filter(model.Admin.id == id).update({
        model.Admin.status: 0})
    session.commit()
    session.close()
