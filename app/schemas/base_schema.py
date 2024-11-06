from typing import Optional
from pydantic import BaseModel

# Base schema class for data validation
class BaseSchema(BaseModel):
    class Config:
        # Enable attribute population from ORM models
        from_attributes = True
        # Allow the use of arbitrary (non-standard or non-Pydantic) types
        arbitrary_types_allowed = True

    # Optional identifier field
    id_key: Optional[int] = None
