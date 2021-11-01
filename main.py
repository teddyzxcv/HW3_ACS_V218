# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Container import Container
import sys
import os.path
from ProgrammingLanguages import ProgrammingLanguages
import os

test_root = "TestInput/"
result_root = "TestOutput/"

# Main function.
def main(argv):
    if len(argv) != 5:
        print("Incorrect input!")
        return
    c = Container()
    # Input by file.
    if argv[1] == "-f":
        input_path = test_root + argv[2]
        if os.path.isfile(input_path):
            c.input_file(input_path)
            print("File input!")
        else:
            print("Incorrect input!")
            return
        # Input by random.
    elif argv[1] == "-n":
        if argv[2].isdigit():
            c.input_random(int(argv[2]))
            print("Random input!")
        else:
            print("Incorrect input!")
            return
    else:
        print("Incorrect input!")
        return
    # Output container.
    c.output(result_root + argv[3], "Filled container!")
    print("Output in file!")
    c.binary_insertion()
    # Output sorted container.
    c.output(result_root + argv[4], "Sorted container!")
    print("Sorted output in file!")


if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    main(sys.argv)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
