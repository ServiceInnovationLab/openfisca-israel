from openfisca_core.model_api import *
from openfisca_israel.entities import *


class is_resident(Variable):
    value_type = bool
    default_value = False
    entity = Person
    label = u"Is a resident of Israel"
    definition_period = MONTH
