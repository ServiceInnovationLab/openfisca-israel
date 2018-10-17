from openfisca_core.model_api import *
from openfisca_israel.entities import *


class is_resident(Variable):
    value_type = bool
    default_value = False
    entity = Person
    label = u"Is a resident of Israel"
    definition_period = MONTH


class age_at_immigration(Variable):
    value_type = int
    default_value = False
    entity = Person
    label = u"Age of person when they immigrated to Israel"
    definition_period = ETERNITY
