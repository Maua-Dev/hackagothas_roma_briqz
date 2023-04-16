import abc

from src.shared.domain.enums.sex_enum import SEX

class Criminal(abc.ABC):
       name: str
       description: str
       sex: SEX