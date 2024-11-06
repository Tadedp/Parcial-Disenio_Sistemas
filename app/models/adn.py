from sqlalchemy import Column, String, Boolean

from models.base_model import BaseModel

class ADNModel(BaseModel):
    __tablename__ = 'dnas' # Specifies that this class will be mapped to a table called "dnas"

    # Unique DNA sequence column - not nullable
    dna = Column(String(255), unique=True, nullable=False)
    
    # Mutant DNA indicator column - not nullable
    is_mutant = Column(Boolean, nullable=False)