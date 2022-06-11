from ..model import engine, Student
from sqlalchemy.orm import sessionmaker


def login(stu):
    stu = Student(stu)
    Session = sessionmaker(bind=engine)
    session = Session()
    stu_obj = session.query(Student).filter(
        Student.username == stu.username and Student.password == stu.password).one()
    session.close()

    if(stu_obj):
        return 1
    else:
        return 0
