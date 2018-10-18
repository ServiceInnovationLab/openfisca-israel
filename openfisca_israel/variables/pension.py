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
    reference = "https://www.btl.gov.il/English%20Homepage/Benefits/Old%20Age%20Insurance/Conditions/coveredinoldage/Pages/Woman.aspx https://www.btl.gov.il/English%20Homepage/Benefits/Old%20Age%20Insurance/Conditions/coveredinoldage/Pages/Man.aspx"

    def formula(person, period, parameters):
        #
        # One must have paid contributions for at least 12 years
        years_contributed = person('pension_contributing_years', period)
        years_required = parameters(period).benefits.pension.required_contributing_years
        #
        # Any Israeli resident born in Israel or who first immigrated
        # before the age of 60-62 is eligible for an old age pension
        # provided he or she meets the conditions of entitlement.
        max_age_at_immigration = parameters(period).benefits.pension.max_age_at_immigration[person('gender', period)]

        return person('is_resident', period) \
            * (years_contributed >= years_required) \
            * (person('born_in_israel', period) + person('age_at_immigration', period) < max_age_at_immigration)


class pension_eligibility_age(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Age of eligiblity for pension"
    reference = "https://www.btl.gov.il/English%20Homepage/Benefits/Old%20Age%20Insurance/Conditions/coveredinoldage/Pages/Woman.aspx"

    def formula(person, period, parameters):
        # One must have paid contributions for at least 12 years
        gender = person('gender', period)
        return parameters(period).benefits.pension.age[gender]


class pension_contributing_years(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Number of years contributing towards the pension"
