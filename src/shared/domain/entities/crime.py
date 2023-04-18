import abc

from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.enums.crime_type import CRIME_TYPE
from src.shared.helpers.errors.domain_errors import EntityError

class Crime(abc.ABC):
    crime_id: int
    responsable_criminal: Criminal.name
    crime_type: CRIME_TYPE

    def __init__(self, crime_id: int, responsable_criminal: Criminal, crime_type:CRIME_TYPE) -> None:
        if crime_id is None:
            raise EntityError("crime_id")
        if type(crime_id) != int:
            raise EntityError("crime_id")
        self.crime_id = crime_id

        if responsable_criminal is None:
            raise EntityError("responsable_criminal")
        if type(responsable_criminal) != Criminal:
            raise EntityError("responsable_criminal")
        self.responsable_criminal = responsable_criminal

        if crime_type is None:
            raise EntityError("crime_type")
        if type(crime_type) != CRIME_TYPE:
            raise EntityError("crime_type")
        self.crime_type = crime_type