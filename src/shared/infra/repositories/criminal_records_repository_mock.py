from typing import List
from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.domain.enums.crime_type import CRIME_TYPE
from src.shared.domain.enums.power_enum import POWER
from src.shared.domain.enums.region_enum import REGION
from src.shared.domain.enums.sex_enum import SEX

from src.shared.domain.repositories.criminal_records_repository_interface import ICriminalRecordsRepository

class CriminalRecordsRepositoryMock(ICriminalRecordsRepository):
    criminal_records_list = []

    def __init__(self):
        self.criminal_records_list = [


                
            CriminalRecord(
            criminal_record_id = 1234,
            
            criminal = Criminal(name = "Joker", description = "extremamente instável e maníaco", sex = SEX.MALE, region = REGION.OSASCO, powers=[POWER.SUPER_INTELLIGENCE, POWER.MANIAC]),
            
            crime_list = [
            Crime(crime_id = 12345, 
                  responsible_criminal = Criminal(name = "Joker"), crime_type= CRIME_TYPE.HOMICIDE)
            ], 
            is_arrested = False, 
            hazard_level = 7),



            CriminalRecord(
            criminal_record_id = 4321,
            
            criminal = Criminal(name = "Penguim", description = "Mafioso, tem influência em toda Gotham", sex = SEX.MALE, region = REGION.PINHEIROS, powers=[POWER.SUPER_INTELLIGENCE]),

            crime_list = [
            Crime(crime_id = 1234, 
                  responsible_criminal = Criminal(name = "Pinguim"), crime_type= CRIME_TYPE.HOMICIDE)
            ], 
            is_arrested = False, 
            hazard_level = 3)
            ]
