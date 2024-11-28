'''
Created by greg-ogs for EPAM DevOps specialization.
Nov 2024
'''

import sys

# Example of the first part

from Classes import Dictionary, Tiket, WordConcatenator

if __name__ == '__main__':
    # For part 1
    # d = Dictionary()
    # d.add("Banana", "A yellow fruit")
    # print(d.lookup("Banana"))  # Output: A yellow fruit
    # print(d.lookup("Apple"))  # Output: Word not found in the dictionary.
    # sys.exit(0)

    # For part 2
    # items_and_costs = {
    #     "apple": 1.00,
    #     "banana": 0.50,
    #     "orange": 1.25
    # }
    # receipt = Tiket(items_and_costs)
    #
    # # Get items bought from user input
    # items_str = input("Enter the items bought, separated by commas: ")
    # items_bought = [item.strip() for item in items_str.split(",")]
    # # items_bought = ["apple", "banana", "grapefruit"]  # Grapefruit is not in the dictionary
    # tax_rate = 0.1  # 10% tax
    #
    # total_cost = receipt.calculate_total(items_bought, tax_rate)
    # print(f"Total cost: ${total_cost:.2f}")

    #For part 3
    words_str = input("Enter the words, separated by commas: ")
    words = [word.strip() for word in words_str.split(",")]
    # words = ["soda", "best", "has", "net", "hello", "yes", "computer"]
    concatenator = WordConcatenator(words)
    result = concatenator.concatenate()
    print(result)  # Output: yes