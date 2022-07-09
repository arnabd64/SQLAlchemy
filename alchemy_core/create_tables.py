from alchemy_core.connection import Connection
from sqlalchemy import MetaData, Table, ForeignKey, Column
from sqlalchemy import String, Float, Integer


class TableCreation:
    
    def __init__(self):
        # create engine
        obj = Connection()
        self.engine = obj.engine
        
        # metadta
        self.meta = MetaData()
        
        
    def createStudents(self):
        students = Table('Students', self.meta,
                        Column('id', String(36), primary_key = True),
                        Column('firstname', String(200), nullable = False),
                        Column('lastname', String(200), nullable = False),
                        Column('email', String(100), nullable = False, unique = True),
                        Column('phone', String(10), nullable = False, unique = True),
                        Column('classroom', Integer, ForeignKey("Classroom.room_number", onupdate = 'CASCADE'))
                        )
        try:
            self.meta.create_all(self.engine)
        except:
            return None
        return students


    def createTeachers(self):
        teachers = Table('Teachers', self.meta,
                        Column('id', String(36), primary_key = True),
                        Column('firstname', String(200), nullable = False),
                        Column('lastname', String(200), nullable = False),
                        Column('email', String(100), nullable = False, unique = True),
                        Column('subject', String(100), nullable = False),
                        Column('classroom', Integer, ForeignKey("Classroom.room_number", onupdate = 'CASCADE'))
                        )
        try:
            self.meta.create_all(self.engine)
        except:
            return None
        return teachers


    def createClassroom(self):
        classroom = Table('Classroom', self.meta,
                        Column('id', String(36), primary_key = True),
                        Column('class', Integer, nullable = False),
                        Column('section', String(1), nullable = False),
                        Column('room_number', Integer, unique = True, nullable = False),
                        Column('max_capacity', Integer)
                        )
        try:
            self.meta.create_all(self.engine)
        except:
            return None
        return classroom