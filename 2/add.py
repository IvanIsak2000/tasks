from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from settings import * 

p1 = Personal('125', 'Iwan', 'S')
session.add(p1)
session.commit()


# if result:
#     print('True')