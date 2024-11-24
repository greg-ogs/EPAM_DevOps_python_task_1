'''
Created by greg-ogs for EPAM DevOps specialization.
Nov 2024
'''

import sys

# Example of the first part

from Task_1_dictionary import Dictionary

if __name__ == '__main__':
    d = Dictionary()
    d.add("Banana", "A yellow fruit")
    print(d.lookup("Banana"))  # Output: A yellow fruit
    print(d.lookup("Apple"))  # Output: Word not found in the dictionary.
    sys.exit(0)