from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

# This is the base for all tables
Base = declarative_base()

def init_db():
    attempt = 0
    max_attempts = 3

    while attempt < max_attempts:
        engine = create_engine('sqlite:///my_first_go88.db', echo=True)

        if engine is not None:
            # Create tables
            Base.metadata.create_all(engine)
            print("Database initialized successfully.")
            return sessionmaker(bind=engine)
        else:
            # If engine did not work, increase attempt count
            print("Error creating database.")
            attempt = attempt + 1

    print("Failed to initialize database after retries.")
    return None

# Create session
Session = scoped_session(init_db())
