from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.enums.power_enum import POWER
from src.shared.domain.enums.region_enum import REGION
from src.shared.domain.enums.sex_enum import SEX
from src.shared.domain.repositories.criminal_repository_interface import ICriminalRepository


class CriminalRepositoryMock(ICriminalRepository):

    criminal_list = []

    def __init__(self):
        self.criminal_list = [
            
            Criminal(name = "Joker", description = "extremamente instável e maníaco", sex = SEX.MALE, region = REGION.OSASCO, powers=[POWER.SUPER_INTELLIGENCE, POWER.MANIAC]),

            Criminal(name = "Penguim", description = "Mafioso, tem influência em toda Gotham", sex = SEX.MALE, region = REGION.PINHEIROS, powers=[POWER.SUPER_INTELLIGENCE])

          ]