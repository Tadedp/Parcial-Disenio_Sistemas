from models.adn import ADNModel
from repositories.base_repository_impl import BaseRepositoryImpl
from schemas import ADNSchema

class ADNRepository(BaseRepositoryImpl):
    def __init__(self):
        # Initialize the repository with ADN-specific model and schema
        super().__init__(ADNModel, ADNSchema)
        
    def count_mutants(self):
        """Count mutant ADN rows."""
        return self.session.query(ADNModel).filter_by(is_mutant=True).count()

    def count_humans(self):
        """Count human ADN rows."""
        return self.session.query(ADNModel).filter_by(is_mutant=False).count()
