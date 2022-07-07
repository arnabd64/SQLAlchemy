from alchemy_core.connection import Connection
from sqlalchemy import MetaData, Table, ForeignKey, Column
from sqlalchemy import String, Float, Integer


# get Engine
obj = Connection()
engine = obj.engine

# Metadata object
meta = MetaData()

# Table 1: Students
students = Table('Students', meta,
                 Column('id', String(36), primary_key = True),
                 Column('firstname', String(200), nullable = False),
                 Column('lastname', String(200), nullable = False),
                 Column('email', String(100), nullable = False, unique = True),
                 Column('phone', String(10), nullable = False, unique = True),
                 Column('classroom', String(36), nullable = False)
                 )

# Table 2: Teachers
teachers = Table('Teachers', meta,
                 Column('id', String(36), primary_key = True),
                 Column('firstname', String(200), nullable = False),
                 Column('lastname', String(200), nullable = False),
                 Column('email', String(100), nullable = False, unique = True),
                 Column('subject', String(100), nullable = False)
                 )

# Table 3: Classroom
classroom = Table('Classroom', meta,
                  Column('id', String(36), primary_key = True),
                  Column('class', Integer, nullable = False),
                  Column('section', String(1), nullable = False),
                  Column('class_teacher', String(36), nullable = False, unique = True),
                  Column('room_number', Integer, unique = True, nullable = False),
                  Column('max_capacity', Integer)
                  )

# Execute
meta.create_all(engine)