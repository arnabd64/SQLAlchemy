import sqlalchemy

# Check Version
print(f"SQLAlchemy version: {sqlalchemy.__version__}")

class Connection:
    
    def __init__(self):
        try:
            self.engine = sqlalchemy.create_engine("sqlite:///sqlite.db")
            print("Created SQLAlchemy Engine")
            print(self.engine)
            
        except Exception as e:
            print(f"Error: {e}")
            