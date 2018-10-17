from openfisca_core.model_api import *
from openfisca_israel.entities import *


class born_in_israel(Variable):
    value_type = bool
    default_value = False
    entity = Person
    label = u"Was born in Israel"
    definition_period = MONTH
