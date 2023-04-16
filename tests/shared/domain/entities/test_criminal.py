import pytest
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.enums.power_enum import POWER
from src.shared.domain.enums.region_enum import REGION
from src.shared.domain.enums.sex_enum import SEX
from src.shared.helpers.errors.domain_errors import EntityError

class Test_Criminal:
       def test_criminal(self):
              criminal = Criminal(name="Jorginho Bala Tensa", description="Um dos violoes mais temidos de todo o oeste", sex=SEX.MALE, region=REGION.CAPAO_REDONDO, powers=[POWER.MANIAC, POWER.ELITE_SHOOTER])

              assert criminal.name == "Jorginho Bala Tensa"
              assert criminal.description == "Um dos violoes mais temidos de todo o oeste"
              assert criminal.sex == SEX.MALE
              assert criminal.region == REGION.CAPAO_REDONDO
              assert criminal.powers == [POWER.MANIAC, POWER.ELITE_SHOOTER]

       def test_criminal_invalid_name(self):
              with pytest.raises(EntityError):
                     criminal = Criminal(name=5, description="Um dos violoes mais temidos de todo o oeste", sex=SEX.MALE, region=REGION.CAPAO_REDONDO, powers=[POWER.MANIAC, POWER.ELITE_SHOOTER])

       def test_criminal_invalid_name_none(self):
              with pytest.raises(EntityError):
                     criminal = Criminal(name=None, description="Um dos violoes mais temidos de todo o oeste", sex=SEX.MALE, region=REGION.CAPAO_REDONDO, powers=[POWER.MANIAC, POWER.ELITE_SHOOTER])
       
       def test_criminal_invalid_description(self):
              with pytest.raises(EntityError):
                     criminal = Criminal(name="Jorginho Bala Tensa", description=456, sex=SEX.MALE, region=REGION.CAPAO_REDONDO, powers=[POWER.MANIAC, POWER.ELITE_SHOOTER])

       def test_criminal_invalid_sex(self):
              with pytest.raises(EntityError):
                     criminal = Criminal(name="Jorginho Bala Tensa", description="Um dos violoes mais temidos de todo o oeste", sex="ALFA", region=REGION.CAPAO_REDONDO, powers=[POWER.MANIAC, POWER.ELITE_SHOOTER])

       def test_criminal_invalid_region(self):
              with pytest.raises(EntityError):
                     criminal = Criminal(name="Jorginho Bala Tensa", description="Um dos violoes mais temidos de todo o oeste", sex=SEX.MALE, region=12-65, powers=[POWER.MANIAC, POWER.ELITE_SHOOTER])

       def test_criminal_invalid_powers(self):
              with pytest.raises(EntityError):
                     criminal = Criminal(name="Jorginho Bala Tensa", description="Um dos violoes mais temidos de todo o oeste", sex=SEX.MALE, region=REGION.CAPAO_REDONDO, powers="EU SOU A VELOCIDADE")