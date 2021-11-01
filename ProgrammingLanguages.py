import random

from AllEnums import *


# Parent class of all languages.
class ProgrammingLanguages:
    # Initialize the class.
    def __init__(self, count_name, toibi, year_of_creation):
        self.count_name = count_name
        self.toibi = toibi
        self.year_of_creation = year_of_creation

    # Function calculate the year divide letters.
    def year_divide_letters(self):
        return self.year_of_creation / self.count_name


# Functional language.
class Functional(ProgrammingLanguages):
    def __init__(self, count_name, toibi, year_of_creation, type: FunctionalTypes, is_lazy_support: bool):
        super().__init__(count_name, toibi, year_of_creation)
        self.type = type
        self.is_lazy_support = is_lazy_support

    # Return random functional language.
    @staticmethod
    def random():
        return Functional(10, random.randint(0, 100), random.randint(1888, 2022),
                          FunctionalTypes(random.randint(1, 2)), bool(random.randint(0, 1)))

    # To string.
    def to_string(self):
        ils = "No"
        if self.is_lazy_support:
            ils = "Yes"
        return f"It is a functional language: TIOBI = {self.toibi}. Year of creation = {self.year_of_creation}. " \
               f"Years divide count letters in the name = {self.year_divide_letters()}. Type = {self.type}. Is lazy " \
               f"calculation support = {ils}.\n"


class ObjectOriented(ProgrammingLanguages):
    def __init__(self, count_name, toibi, year_of_creation, inheritance: ObjectOrientedInheritance):
        super().__init__(count_name, toibi, year_of_creation)
        self.inheritance = inheritance

    # Return random functional language.
    @staticmethod
    def random():
        return ObjectOriented(14, random.randint(0, 100), random.randint(1888, 2022),
                              ObjectOrientedInheritance(random.randint(1, 3)))

    # To string.
    def to_string(self):
        return f"It is a object oriented language: TIOBI = {self.toibi}. Year of creation = {self.year_of_creation}. " \
               f"Years divide count letters in the name = {self.year_divide_letters()}. Inheritance = {self.inheritance}.\n"


class Procedural(ProgrammingLanguages):
    def __init__(self, count_name, toibi, year_of_creation, is_abstract: bool):
        super().__init__(count_name, toibi, year_of_creation)
        self.is_abstract = is_abstract

    # Return random functional language.
    @staticmethod
    def random():
        return Procedural(14, random.randint(0, 100), random.randint(1888, 2022),
                          bool(random.randint(0, 1)))

    # To string.
    def to_string(self):
        iate = "No"
        if self.is_abstract:
            iate = "Yes"
        return f"It is a procedural language: TIOBI = {self.toibi}. Year of creation = {self.year_of_creation}. " \
               f"Years divide count letters in the name = {self.year_divide_letters()}. Is abstract type exist = {iate}.\n"
