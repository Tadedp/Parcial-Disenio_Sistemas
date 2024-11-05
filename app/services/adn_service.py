from models.adn import ADNModel
from repositories.adn_repository import ADNRepository
from schemas.adn_schema import ADNSchema
from services.base_service_impl import BaseServiceImpl

class ADNService(BaseServiceImpl):
    def __init__(self):
        super().__init__(repository=ADNRepository(), model=ADNModel, schema=ADNSchema)
    
    def get_stats(self) -> dict[str, float]:
        total_mutant_dna: int = self.repository.count_mutants()
        total_human_dna: int = self.repository.count_humans()
        ratio: float = 0.0
        
        if total_human_dna > 0:
            ratio = total_mutant_dna / total_human_dna 

        return {
            "count_mutant_dna": total_mutant_dna,
            "count_human_dna": total_human_dna,
            "ratio": ratio
        }
     
    def isMutant(self, dna: list[str]) -> bool:
        rows_count: int = len(dna)
        cols_count: int = len(dna[0])
        
        horizontal_count: list[list[int]] = [[0] * cols_count for _ in range(rows_count)]
        vertical_count: list[list[int]] = [[0] * cols_count for _ in range(rows_count)]
        diagonal_right_count: list[list[int]] = [[0] * cols_count for _ in range(rows_count)]
        diagonal_left_count: list[list[int]] = [[0] * cols_count for _ in range(rows_count)]

        sequence_count: int = 0
        
        for i in range(rows_count):
            for j in range(cols_count):
                if dna[i][j] in ['A', 'T', 'C', 'G']:
 
                    if j > 0 and dna[i][j] == dna[i][j - 1]:
                        horizontal_count[i][j] = horizontal_count[i][j - 1] + 1
                    else:
                        horizontal_count[i][j] = 1

                    if horizontal_count[i][j] % 4 == 0:
                        sequence_count += 1
                        if sequence_count > 1:
                            return True


                    if i > 0 and dna[i][j] == dna[i - 1][j]:
                        vertical_count[i][j] = vertical_count[i - 1][j] + 1
                    else:
                        vertical_count[i][j] = 1

                    if vertical_count[i][j] % 4 == 0:
                        sequence_count += 1
                        if sequence_count > 1:
                            return True

                    if i > 0 and j > 0 and dna[i][j] == dna[i - 1][j - 1]:
                        diagonal_right_count[i][j] = diagonal_right_count[i - 1][j - 1] + 1
                    else:
                        diagonal_right_count[i][j] = 1

                    if diagonal_right_count[i][j] % 4 == 0:
                        sequence_count += 1
                        if sequence_count > 1:
                            return True


                    if i > 0 and j < cols_count - 1 and dna[i][j] == dna[i - 1][j + 1]:
                        diagonal_left_count[i][j] = diagonal_left_count[i - 1][j + 1] + 1
                    else:
                        diagonal_left_count[i][j] = 1

                    if diagonal_left_count[i][j] % 4 == 0:
                        sequence_count += 1
                        if sequence_count > 1:
                            return True

        return False