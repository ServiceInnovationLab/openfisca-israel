# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_israel.entities import *


class pension_eligibility_age(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Age of eligiblity for pension"
    reference = "https://github.com/ServiceInnovationLab/Piccolo/issues/4"

    # Since Dec 1st 2016, the basic income is provided to any adult, without considering their income.
    def formula(person, period, parameters):
        gender = person('gender', period)
        return parameters(period).general.pension_age[gender]

