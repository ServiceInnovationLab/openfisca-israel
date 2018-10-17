# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_israel.entities import *


class eligible_for_pension(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Eligiblity for pension"
    reference = "https://github.com/ServiceInnovationLab/Piccolo/issues/4"

    def formula(person, period, parameters):
        #
        # One must have paid contributions for at least 12 years
        years_required = parameters(period).general.pension_contribution_years
        years_contributed = person('pension_contributing_years', period)
        #
        # Any Israeli resident born in Israel or who first immigrated
        # before the age of 60-62 is eligible for an old age pension
        # provided he or she meets the conditions of entitlement.
        resident = person('is_resident', period)

        return resident * (years_contributed >= years_required)


class pension_eligibility_age(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Age of eligiblity for pension"
    reference = "https://github.com/ServiceInnovationLab/Piccolo/issues/4"

    def formula(person, period, parameters):
        # One must have paid contributions for at least 12 years
        gender = person('gender', period)
        return parameters(period).general.pension_age[gender]


class pension_contributing_years(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Number of years contributing towards the pension"
