'''
Create SQLAlchemy engine
'''

import sqlalchemy

# Check Version
print(f"SQLAlchemy version: {sqlalchemy.__version__}")

class Connection:
    
    def __init__(self):
        try:
            self.engine = sqlalchemy.create_engine("sqlite:///sqlite.db", echo = True)
        except Exception as e:
            print(f"Error: {e}")
            