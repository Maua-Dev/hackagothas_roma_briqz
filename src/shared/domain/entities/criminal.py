import abc
from typing import List
from src.shared.domain.enums.region_enum import REGION

from src.shared.domain.enums.sex_enum import SEX
from src.shared.domain.enums.power_enum import POWER
from src.shared.helpers.errors.domain_errors import EntityError

class Criminal(abc.ABC):
       name: str
       description: str
       sex: SEX
       region: REGION
       powers: List[POWER]
       MIN_NAME_LENGTH = 2

       def __init__(self, name:str, description:str, sex:SEX, region:REGION, powers:List[POWER]) -> None:
              if not Criminal.validate_name(name):
                     raise EntityError("name")
              self.name = name

              if type(description) != str:
                     raise EntityError("description")
              self.description = description

              if type(sex) != SEX:
                     raise EntityError("sex")
              self.sex = sex

              if type(region) != REGION:
                     raise EntityError("region")
              self.region = region
              
              if not Criminal.validate_powers(powers):
                     raise EntityError("powers")
              self.powers = powers
              
       @staticmethod
       def validate_name(name: str) -> bool:
              if name is None:
                     return False
              elif type(name) != str:
                     return False
              elif len(name) < Criminal.MIN_NAME_LENGTH:
                     return False
                     
              return True
              
       @staticmethod
       def validate_powers(powers: List[POWER]) -> bool:
              if powers is None:
                     return False
              elif type(powers) != list:
                     return False
              elif len(powers) < 1:
                     return False
              elif not all(isinstance(power, POWER) for power in powers):
                     return False
              return True
