from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Users(Base):
    __tablename__ = 'Users'


    id = Column(Integer, primary_key=True)
    name = Column(Integer)
    surname = Column(String)
