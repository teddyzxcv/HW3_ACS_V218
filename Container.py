import random

import AllEnums
from ProgrammingLanguages import *


class Container:

    def __init__(self):
        self.languages_list = []

    def input_file(self, file_path):
        with open(file_path, "r") as file:
            size = file.readline()
            lines = file.readlines()
            for line in lines:
                parameters = line.split()
                language = ProgrammingLanguages(0, 0, 0)
                if int(parameters[0]) == 1:
                    language = Functional(10, float(parameters[1]), int(parameters[2]),
                                          AllEnums.FunctionalTypes(int(parameters[3])),
                                          bool(parameters[4]))
                elif int(parameters[0]) == 2:
                    language = ObjectOriented(14, float(parameters[1]), int(parameters[2]),
                                              AllEnums.ObjectOrientedInheritance(int(parameters[3])))
                elif int(parameters[0]) == 3:
                    language = Procedural(10, float(parameters[1]), int(parameters[2]),
                                          bool(parameters[3]))
                self.languages_list.append(language)
            file.close()

    def input_random(self, size):
        for i in range(size):
            language = ProgrammingLanguages(0, 0, 0)
            select = random.randint(1, 3)
            if select == 1:
                language = Functional.random()
            elif select == 2:
                language = ObjectOriented.random()
            elif select == 3:
                language = Procedural.random()
            self.languages_list.append(language)

    def output(self, filepath, argument):
        with open(filepath, "w") as file:
            file.write(f"{argument}\nContainer contains {len(self.languages_list)} elements.\n")
            counter = 0
            for language in self.languages_list:
                file.write(f"{counter}: " + language.to_string())
                counter = counter + 1
            file.close()

    def binary_search(self, item: ProgrammingLanguages, low: int, high: int):
        if high <= low:
            if item.year_divide_letters() < self.languages_list[low].year_divide_letters():
                return low + 1
            else:
                return low
        mid: int = int(int(low + high) / 2)
        if item.year_divide_letters() == self.languages_list[mid].year_divide_letters():
            return mid + 1
        if item.year_divide_letters() < self.languages_list[mid].year_divide_letters():
            return self.binary_search(item, mid + 1, high)
        return self.binary_search(item, low, mid - 1)

    def binary_insertion(self):
        j: int = 0
        loc: int = 0
        selected: ProgrammingLanguages = self.languages_list[0]
        for i in range(len(self.languages_list)):
            j = i - 1
            selected = self.languages_list[i]
            loc = self.binary_search(selected, 0, j)
            while j >= loc:
                self.languages_list[j + 1] = self.languages_list[j]
                j = j - 1
            self.languages_list[j + 1] = selected
