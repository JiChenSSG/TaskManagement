from pstats import Stats
from sqlalchemy import create_engine, null, nullslast
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    sex = Column(String(2), nullable=False)
    grade = Column(Integer, nullable=False)
    city = Column(String(50), nullable=False)
    status = Column(Integer, nullable=False)

    def __init__(self, name, age, sex, grade, city, status):
        self.name = name
        self.age = age
        self.sex = sex
        self.grade = grade
        self.city = city
        self.status = status


class Admin(Base):
    __tablename__ = 'admin'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    status = Column(Integer, nullable=False)

    def __init__(self, username, password, status):
        self.username = username
        self.password = password
        self.status = status


class Tasks(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    taskName = Column(String(50), nullable=False)
    date = Column(DateTime, nullable=False)
    status = Column(Integer, nullable=False)

    def __init__(self, taskName, date, status):
        self.taskName = taskName
        self.date = date
        self.status = status


class TaskDetails(Base):
    __tablename__ = 'task_details'
    id = Column(Integer, primary_key=True, autoincrement=True)
    taskId = Column(Integer, ForeignKey('tasks.id'), nullable=False)
    studentId = Column(Integer, ForeignKey('student.id'), nullable=False)
    score = Column(Integer, nullable=False)
    status = Column(Integer, nullable=False)

    def __init__(self, taskId, studentId, score, status):
        self.taskId = taskId
        self.studentId = studentId
        self.score = score
        self.status = status


engine = create_engine(
    "mysql+pymysql://root:123456@127.0.0.1/python?charset=utf8")
Base.metadata.create_all(engine)
