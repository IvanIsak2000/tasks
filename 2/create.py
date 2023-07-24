from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Personal(Base):
    __tablename__ = 'personal'

    ssn = Column('ssn', Integer, primary_key=True)
    firstname = Column('firstname', String)
    lastname = Column('lastname', String)

    def __init__(self, ssn, firstname, lastname):
        self.ssn = ssn
        self.firstname = firstname
        self.lastname = lastname

engine = create_engine('sqlite:///example.db')
Base.metadata.create_all(bind=engine)