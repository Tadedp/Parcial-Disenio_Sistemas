from fastapi import HTTPException

from controllers.base_controller_impl import BaseControllerImpl
from schemas.adn_schema import ADNSchema
from services.adn_service import ADNService


class ADNController(BaseControllerImpl):
    def __init__(self):
        super().__init__(ADNSchema, ADNService())
        
        @self.router.get("/stats")
        async def get_stats():
            return self.get_stats()

        @self.router.post("/")
        async def is_mutant(schema_in: ADNSchema):
            return self.is_mutant(schema_in)
        
    def get_stats(self) -> list[ADNSchema]:
        """Get all DNA stats."""
        return self.service.get_stats()
    
    def is_mutant(self, schema: ADNSchema) -> ADNSchema:
        """Check ADN."""
        dna_sequence = schema.dna

        if not dna_sequence:
            raise HTTPException(status_code=400, detail="DNA sequence is required.")
        
        if self.service.isMutant(dna_sequence):
            schema.is_mutant = True
            try:
                self.service.save(schema)
            except Exception:
                raise HTTPException(status_code=409, detail="DNA sequence already exists.")
            return {"detail": "Mutant DNA."}
        else:
            schema.is_mutant = False
            try:
                self.service.save(schema)
            except Exception:
                raise HTTPException(status_code=409, detail="DNA sequence already exists.")
            raise HTTPException(status_code=403, detail="Human DNA.")