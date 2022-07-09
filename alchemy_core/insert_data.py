from alchemy_core.connection import Connection
from alchemy_core.create_tables import TableCreation

from uuid import uuid4

class DataInput:
    
    def __init__(self):
        obj = Connection()
        self.cnx = obj.engine.connect()
        
    
    def students(self, values: dict):
        '''
        Method to insert data into the Students Table.
        The data has to be passed as a Python dictionary:
        
        values = {
            "firstname" : "John",
            "lastname" : "Doe",
            "email" : "johndoe@mail.com",
            "phone" : "1234567890",
            "classroom" : 1408
        }
        '''
        # set id
        values['id'] = str(uuid4())
        
        # get Students object
        obj = TableCreation()
        students = obj.createStudents()
        
        # Execute
        try:
            response = self.cnx.execute(students.insert(), values)
            self.cnx.commit()
        except Exception as e:
            return {"error":1, "message":e}
        
        return {"error":0, "message": response}
    
    
    def teachers(self, values: dict):
        '''
        Method to insert data into the Teachers Table.
        The data has to be passed as a Python dictionary:
        
        values = {
            "firstname" : "John",
            "lastname" : "Doe",
            "email" : "johndoe@mail.com",
            "subject" : "Mathematics",
            "classroom" : 1408
        }
        '''
        # set id
        values['id'] = str(uuid4())
        
        # get Students object
        obj = TableCreation()
        teahchers = obj.createTeachers()
        
        # Execute
        try:
            response = self.cnx.execute(teahchers.insert(), values)
            self.cnx.commit()
        except Exception as e:
            return {"error":1, "message":e}
        
        return {"error":0, "message": response}
    
    
    def classroom(self, values: dict):
        '''
        Method to insert data into the Teachers Table.
        The data has to be passed as a Python dictionary:
        
        values = {
            "class" : 10,
            "section" : "A",
            "room_number" : 1221,
            "max_capacity" : 40
        }
        '''
        