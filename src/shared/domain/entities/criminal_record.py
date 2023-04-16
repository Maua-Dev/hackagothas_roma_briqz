from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.enums.crime_type import CRIME_TYPE
import abc 
import re
from typing import List

from src.shared.helpers.errors.domain_errors import EntityError


class CriminalRecord(abc.ABC):
    
    criminal_record_id: int
    criminal: Criminal
    crime_list: List[Crime]
    is_arrested : bool
    hazard_level: int

    def __init__(self, criminal_record_id: int, criminal: Criminal,
                  crime_list: List[Crime], is_arrested:bool, hazard_level: int):
        
        if not CriminalRecord.validate_criminal_record_id(criminal_record_id):
            raise EntityError("criminal_record_id")
        self.criminal_record_id = criminal_record_id

        
        
        if type(criminal_record_id) == int:
            if criminal_record_id < 0:
                raise EntityError("criminal_record_id")
        
        
        @staticmethod
        def validate_criminal_record_id(criminal_record_id:int) -> bool:
            if criminal_record_id is None:
                return False
            elif type(criminal_record_id) != int:
                return False

        @staticmethod
        def validate_hazard_level(hazard_level:int)->bool:
            if type(hazard_level) == int:
                if hazard_level>10 or hazard_level<0:
                 return False
            else:
                return False
            
    
    def __repr__(self):
        return f"CriminalRecord(criminal_record_id={self.crime_list}, crime_list={self.crime_list}, criminal={self.criminal}, \
                crime_list={self.crime_list},is_arrested={self.is_arrested},hazard_level={self.hazard_level})"  