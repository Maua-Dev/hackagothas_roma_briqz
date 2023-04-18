


from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.enums.crime_type import CRIME_TYPE
from src.shared.domain.repositories.crime_repository_interface import ICrimeRepository


class CrimeRepositoryMock(ICrimeRepository):

    
    crime_list = []
    def __init__(self):
        
        self.crime_list = [
            Crime(crime_id = 12345, responsible_criminal = Criminal(name = "Joker"), crime_type= CRIME_TYPE.HOMICIDE),

            Crime(crime_id = 1234, responsible_criminal = Criminal(name = "Pinguim"), crime_type= CRIME_TYPE.HOMICIDE)
        
        ]
