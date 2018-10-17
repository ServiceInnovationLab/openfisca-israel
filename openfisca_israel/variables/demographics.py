# -*- coding: utf-8 -*-
from openfisca_core.model_api import *
from openfisca_israel.entities import *


# This variable is a pure input: it doesn't have a formula
class birth(Variable):
    value_type = date
    # By default, if no value is set for a simulation,
    # we consider the people involved in a simulation
    # to be born on the 1st of Jan 1970.
    default_value = date(1970, 1, 1)
    entity = Person
    label = u"Birth date"
    definition_period = ETERNITY  # This variable cannot change over time.
    reference = u"https://en.wiktionary.org/wiki/birthdate"


class age(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = u"Person's age (in years)"

    # A person's age is computed according to its birth date.
    def formula(person, period, parameters):
        birth = person('birth', period)
        birth_year = birth.astype('datetime64[Y]').astype(int) + 1970
        birth_month = birth.astype('datetime64[M]').astype(int) % 12 + 1
        birth_day = (birth - birth.astype('datetime64[M]') + 1).astype(int)

        is_birthday_past = (birth_month < period.start.month) + (birth_month ==
                                                                 period.start.month) * (birth_day <= period.start.day)

        # If the birthday is not passed this year, subtract one year
        return (period.start.year - birth_year) - where(is_birthday_past, 0, 1)


class Genders(Enum):
    __order__ = "man woman unspecified"
    woman = u'Woman'
    man = u'Man'
    unspecified = u'Unspecified'


class gender(Variable):
    value_type = Enum
    possible_values = Genders
    default_value = Genders.unspecified
    entity = Person
    definition_period = MONTH
    label = u"A Person's gender"
