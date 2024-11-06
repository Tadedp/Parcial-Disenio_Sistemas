from fastapi import HTTPException

from controllers.base_controller_impl import BaseControllerImpl
from schemas.adn_schema import ADNSchema
from services.adn_service import ADNService


class ADNController(BaseControllerImpl):
    def __init__(self):
        # Initialize the controller with ADN-specific service and schema
        super().__init__(ADNSchema, ADNService())
        
        # Define GET route to fetch DNA statistics
        @self.router.get("/stats")
        async def get_stats():
            # Call the controller's get_stats method to retrieve stats
            return self.get_stats()

        # Define POST route to check if DNA sequence is mutant
        @self.router.post("/")
        async def is_mutant(schema_in: ADNSchema):
            # Call the controller's is_mutant method to check DNA
            return self.is_mutant(schema_in)
        
    def get_stats(self) -> list[ADNSchema]:
        """Get all DNA stats."""
        return self.service.get_stats()
    
    def is_mutant(self, schema: ADNSchema) -> ADNSchema:
        """Check ADN."""
        dna_sequence = schema.dna # Extract DNA sequence from schema

        # Raise exception if DNA sequence is missing
        if not dna_sequence:
            raise HTTPException(status_code=400, detail="DNA sequence is required.")
        
        # Call service to check if DNA is mutant
        if self.service.isMutant(dna_sequence):
            # If mutant, set the schema's is_mutant attribute to True
            schema.is_mutant = True
            
            try:
                self.service.save(schema)
            except Exception:
                # Raise HTTP 409 if DNA sequence already exists
                raise HTTPException(status_code=409, detail="DNA sequence already exists.")
            
            # HTTP 200 OK response for mutant DNA
            return {"detail": "Mutant DNA."}
        else:
            # If not mutant, set the schema's is_mutant attribute to False
            schema.is_mutant = False
            
            try:
                self.service.save(schema)
            except Exception:
                # Raise HTTP 409 if DNA sequence already exists
                raise HTTPException(status_code=409, detail="DNA sequence already exists.")
            
            # Raise HTTP 403 for human DNA
            raise HTTPException(status_code=403, detail="Human DNA.")