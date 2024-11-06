from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

# Define a base class that models can inherit from to use SQLAlchemy's ORM features and define tables as Python classes.
base = declarative_base()

class BaseModel(base):
    __abstract__ = True # Specifies that this class is abstract and won’t be mapped to a table

    # Primary key column for uniquely identifying records in the table
    id_key = Column(Integer, primary_key=True) 
