
    # criminal_record_id: int
    # criminal: Criminal
    # crime_list: List[Crime]
    # is_arrested : bool
    # hazard_level: int

from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.enums.crime_type import CRIME_TYPE
from src.shared.domain.enums.power_enum import POWER
from src.shared.domain.enums.region_enum import REGION
from src.shared.domain.enums.sex_enum import SEX


class Test_Criminal_Record:

    def test_criminal_record_id(self):
        criminal = Criminal(name="Jorginho Bala Tensa", description="Um dos violoes mais temidos de todo o oeste", sex=SEX.MALE, region=REGION.CAPAO_REDONDO, powers=[POWER.MANIAC, POWER.ELITE_SHOOTER])
        crime = Crime(crime_id=123, responsable_criminal=criminal, crime_type=CRIME_TYPE.ASSAULT)
    
        criminal_record = CriminalRecord(
            criminal_record_id=123, 
            criminal =criminal,
            crime_list = [crime],
            is_arrested = True,
            hazard_level = 10
            )
    
        assert type(criminal_record) == CriminalRecord