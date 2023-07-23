from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Person_table(Base):
    __tablename__ = 'person'

    ssn = Column('ssn', Integer, primary_key=True)
    firstname = Column('firstname', String)
    lastname = Column('lastname', String)
    gender = Column('gender', CHAR)
    age = Column('age', Integer)

    def __init__(self, ssn, firstname, lastname, gender, age):
        self.ssn = ssn
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age


engine = create_engine('sqlite:///example.db', echo=False)

Session = sessionmaker(bind=engine)
session = Session()



number = int(input('Number: '))
name = input('Name: ')
lastname = input('Lastname: ')
gender = input('Gender')
age = int(input('Age:'))

new_user = Person_table(number, name, lastname, gender, age)
session.add(new_user)


session.commit()
