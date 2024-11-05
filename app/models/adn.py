from sqlalchemy import Column, String, Boolean

from models.base_model import BaseModel

class ADNModel(BaseModel):
    __tablename__ = 'dnas'

    dna = Column(String(255), unique=True, nullable=False)
    is_mutant = Column(Boolean, nullable=False)