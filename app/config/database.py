import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import OperationalError

from models.base_model import base
from models.adn import ADNModel  # noqa - Import ADNModel to ensure it is loaded by SQLAlchemy (no usage in this file)

# Define the path for the .env file
env_path = os.path.join(os.path.dirname(__file__), '../.env')
load_dotenv(env_path)  # Load environment variables from the .env file

# Fetch database connection details from environment variables
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')

# Construct the database URI (connection string) for PostgreSQL
DATABASE_URI = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'

class Database:
    _instance = None  # Ensures only one instance of the class exists
    engine = create_engine(DATABASE_URI) # Create the engine using the PostgreSQL URI
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # Session factory for database sessions

    def __init__(self):
        self._session = None

    def __new__(cls):
        if not cls._instance:
            # Create a new instance if none exists
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._engine = cls.engine
            cls._instance._SessionLocal = cls.SessionLocal
            
        return cls._instance  # Return the single instance of the class

    def get_session(self) -> Session:
        if self._session is None:
            self._session = self._SessionLocal()  # Create a new session if none exists
        return self._session

    def drop_database(self):
        try:
            base.metadata.drop_all(self._engine) # Drop tables using the metadata of the base model
            print("Tables dropped.")
        except Exception as e:
            print(f"Error dropping tables: {e}")

    def create_tables(self):
        try: 
            base.metadata.create_all(self.engine) # Create tables using the metadata of the base model
            print("Tables created.")
        except Exception as e:
            print(f"Error creating tables: {e}")

    def close_session(self):
        if hasattr(self, "_session"):
            self._session.close() # Close session
            del self._session # Delete the session attribute

    def check_connection(self):
        try:
            # Establish a connection to the database
            with self._engine.connect() as connection: 
                connection.execute(text("SELECT 1"))  # Execute a simple query to check the connection
            print("Connection established.")
            return True
        except Exception as e:
            print(f"Error connecting to database: {e}")
            return False # Return False if the connection fails
