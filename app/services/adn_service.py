from models.adn import ADNModel
from repositories.adn_repository import ADNRepository
from schemas.adn_schema import ADNSchema
from services.base_service_impl import BaseServiceImpl

class ADNService(BaseServiceImpl):
    def __init__(self):
        # Initialize the service with ADN-specific repository, model and schema
        super().__init__(repository=ADNRepository(), model=ADNModel, schema=ADNSchema)
    
    # Method to retrieve DNA stats
    def get_stats(self) -> dict[str, float]:
        # Count total mutant DNA entries
        total_mutant_dna: int = self.repository.count_mutants()
        # Count total human DNA entries
        total_human_dna: int = self.repository.count_humans()
        
        # Calculate ratio of mutants to humans
        ratio: float = 0.0
        if total_human_dna > 0:
            ratio = total_mutant_dna / total_human_dna 

        return {
            "count_mutant_dna": total_mutant_dna,
            "count_human_dna": total_human_dna,
            "ratio": ratio
        }
     
    # Method to determine if a DNA sequence belongs to a mutant
    def isMutant(self, dna: list[str]) -> bool:
        # Number of rows and columns in the DNA matrix
        rows_count: int = len(dna)
        cols_count: int = len(dna[0])
        
        # Initialize matrices to keep track of sequences found in each direction
        horizontal_count: list[list[int]] = [[0] * cols_count for _ in range(rows_count)]
        vertical_count: list[list[int]] = [[0] * cols_count for _ in range(rows_count)]
        diagonal_right_count: list[list[int]] = [[0] * cols_count for _ in range(rows_count)]
        diagonal_left_count: list[list[int]] = [[0] * cols_count for _ in range(rows_count)]

        sequence_count: int = 0
        
        # Iterate through each cell in the DNA matrix. Returns True if more than two sequence of 4 are found in any direction
        for i in range(rows_count):
            for j in range(cols_count):
                # Check if the character is valid DNA (A, T, C, or G)
                if dna[i][j] in ['A', 'T', 'C', 'G']:
                    
                    # Horizontal sequence check
                    if j > 0 and dna[i][j] == dna[i][j - 1]:
                        horizontal_count[i][j] = horizontal_count[i][j - 1] + 1
                    else:
                        horizontal_count[i][j] = 1

                    if horizontal_count[i][j] % 4 == 0:
                        sequence_count += 1
                        if sequence_count > 1:
                            return True

                    # Vertical sequence check
                    if i > 0 and dna[i][j] == dna[i - 1][j]:
                        vertical_count[i][j] = vertical_count[i - 1][j] + 1
                    else:
                        vertical_count[i][j] = 1

                    if vertical_count[i][j] % 4 == 0:
                        sequence_count += 1
                        if sequence_count > 1:
                            return True

                    # Diagonal (top-left to bottom-right) sequence check
                    if i > 0 and j > 0 and dna[i][j] == dna[i - 1][j - 1]:
                        diagonal_right_count[i][j] = diagonal_right_count[i - 1][j - 1] + 1
                    else:
                        diagonal_right_count[i][j] = 1

                    if diagonal_right_count[i][j] % 4 == 0:
                        sequence_count += 1
                        if sequence_count > 1:
                            return True

                    # Diagonal (top-right to bottom-left) sequence check
                    if i > 0 and j < cols_count - 1 and dna[i][j] == dna[i - 1][j + 1]:
                        diagonal_left_count[i][j] = diagonal_left_count[i - 1][j + 1] + 1
                    else:
                        diagonal_left_count[i][j] = 1

                    if diagonal_left_count[i][j] % 4 == 0:
                        sequence_count += 1
                        if sequence_count > 1:
                            return True
                        
        # If no two or more mutant sequences are found, return False
        return False