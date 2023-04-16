
    # criminal_record_id: int
    # criminal: Criminal
    # crime_list: List[Crime]
    # is_arrested : bool
    # hazard_level: int

from src.shared.domain.entities import criminal_record
from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal


class Test_Criminal_Record:

    def test_criminal_record_id(self):
    
        criminal_record = CriminalRecord(
            criminal_record_id=123, 
            criminal =Criminal(id= 312, nome= "joker"),
            crime_list = [
            Crime(),
            ],
            is_arrested = True,
            hazard_level = 10
            )
    
    assert type(criminal_record) == CriminalRecord