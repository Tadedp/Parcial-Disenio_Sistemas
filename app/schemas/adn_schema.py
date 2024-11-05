from typing import Optional, List

from schemas.base_schema import BaseSchema

class ADNSchema(BaseSchema):
    dna: Optional[list[str]] = None
    is_mutant: Optional[bool] = None