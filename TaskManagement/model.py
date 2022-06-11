from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    status = Column(Integer, nullable=False)

    def __init__(self, username, password, status):
        self.username = username
        self.password = password
        self.status = status


class Teacher(Base):
    __tablename__ = 'teacher'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    status = Column(Integer, nullable=False)

    def __init__(self, username, password, status):
        self.username = username
        self.password = password
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


from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:123456@127.0.0.1/python?charset=utf8")
Base.metadata.create_all(engine)