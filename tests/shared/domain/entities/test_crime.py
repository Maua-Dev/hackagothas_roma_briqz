from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.enums.crime_type import CRIME_TYPE
from src.shared.domain.enums.power_enum import POWER
from src.shared.domain.enums.region_enum import REGION
from src.shared.domain.enums.sex_enum import SEX
import pytest

from src.shared.helpers.errors.domain_errors import EntityError

class Test_Crime():

       def test_crime(self):
              criminal = Criminal(name="Jorginho Bala Tensa", description="Um dos violoes mais temidos de todo o oeste", sex=SEX.MALE, region=REGION.CAPAO_REDONDO, powers=[POWER.MANIAC, POWER.ELITE_SHOOTER])
              crime = Crime(crime_id=2, responsable_criminal=criminal, crime_type=CRIME_TYPE.ASSAULT)

              assert crime.crime_id == 2
              assert crime.responsable_criminal == criminal
              assert crime.crime_type == CRIME_TYPE.ASSAULT

       def test_crime_id_is_none(self):
              criminal = Criminal(name="Jorginho Bala Tensa", description="Um dos violoes mais temidos de todo o oeste", sex=SEX.MALE, region=REGION.CAPAO_REDONDO, powers=[POWER.MANIAC, POWER.ELITE_SHOOTER])
              with pytest.raises(EntityError):
                     crime = Crime(crime_id=None, responsable_criminal=criminal, crime_type=CRIME_TYPE.ASSAULT)
       
       def test_crime_invalid_crime_id(self):
              criminal = Criminal(name="Jorginho Bala Tensa", description="Um dos violoes mais temidos de todo o oeste", sex=SEX.MALE, region=REGION.CAPAO_REDONDO, powers=[POWER.MANIAC, POWER.ELITE_SHOOTER])
              with pytest.raises(EntityError):
                     crime = Crime(crime_id="INVALIDO", responsable_criminal=criminal, crime_type=CRIME_TYPE.ASSAULT)

       def test_crime_responsable_criminal_is_none(self):
              with pytest.raises(EntityError):
                     crime = Crime(crime_id=5, responsable_criminal=None, crime_type=CRIME_TYPE.ASSAULT)

       def test_crime_invalid_responsable_criminal(self):
              with pytest.raises(EntityError):
                     crime = Crime(crime_id=5, responsable_criminal="Joker", crime_type=CRIME_TYPE.ASSAULT)

       def test_crime_type_is_none(self):
              criminal = Criminal(name="Jorginho Bala Tensa", description="Um dos violoes mais temidos de todo o oeste", sex=SEX.MALE, region=REGION.CAPAO_REDONDO, powers=[POWER.MANIAC, POWER.ELITE_SHOOTER])
              with pytest.raises(EntityError):
                     crime = Crime(crime_id=5, responsable_criminal=criminal, crime_type=None)

       def test_crime_invalid_crime_type(self):
              criminal = Criminal(name="Jorginho Bala Tensa", description="Um dos violoes mais temidos de todo o oeste", sex=SEX.MALE, region=REGION.CAPAO_REDONDO, powers=[POWER.MANIAC, POWER.ELITE_SHOOTER])
              with pytest.raises(EntityError):
                     crime = Crime(crime_id=5, responsable_criminal=criminal, crime_type="MASCULO")