from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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

    def __repr__(self):
        return f'{self.ssn} {self.firstname} {self.lastname}'

engine = create_engine('sqlite:///example.db')
Session = sessionmaker(bind=engine)
session = Session()


user = session.query(Personal).filter(Personal.firstname == 'Iwan').first()
#     print(r)
if user:
    print(user.ssn, user.lastname)
