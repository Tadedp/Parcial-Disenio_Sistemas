from typing import Optional, List

from schemas.base_schema import BaseSchema

class ADNSchema(BaseSchema):
    # Optional DNA sequence field
    dna: Optional[list[str]] = None
    
    # Optional mutant DNA indicator field
    is_mutant: Optional[bool] = None