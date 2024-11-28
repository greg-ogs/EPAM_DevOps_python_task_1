import sys

class Dictionary:
    def __init__(self):
        # Initializes an empty dictionary.
        self.words = {}

    def add(self, word, entry):
        """
        Adds a word and its entry to the dictionary.

        Args:
          word: The word to add.
          entry: The entry for the word.
        """
        self.words[word] = entry

    def lookup(self, word):
        """
        Looks up a word in the dictionary and returns its entry.

        Args:
          word: The word to look up.

        Returns:
          The entry for the word, or a message indicating that the word is
          not in the dictionary.
        """
        if word in self.words:
            return self.words[word]
        else:
            return "Word not found in the dictionary."

class Tiket:
    """
    Calculates the total cost of items purchased, including tax.
    """

    def __init__(self, items_and_costs):
        """
        Initializes the Receipt with a dictionary of items and their costs.

        Args:
          items_and_costs: A dictionary where keys are item names (str)
                            and values are their corresponding costs (float).
        """
        self.items_and_costs = items_and_costs

    def calculate_total(self, items_bought, tax_rate):
        """
        Calculates the total cost of the items in the list,
        including tax, ignoring items not in the dictionary.

        Args:
          items_bought: A list of items purchased (str).
          tax_rate: The tax rate as a decimal (float).

        Returns:
          The total cost with two decimal places (float).
        """
        total_cost = 0
        for item in items_bought:
            if item in self.items_and_costs:
                total_cost += self.items_and_costs[item]
        total_cost += total_cost * tax_rate # Tax
        return round(total_cost, 2)

class WordConcatenator:
    """
    Concatenates the nth letter of each word in a list to create a new word.
    """
    def __init__(self, words):
        """
        Args:
        words: A list of words (str).
        """
        self.words = words

    def concatenate(self):
        """
        Concatenates the nth letter of each word in the list.

        Args:
          words: A list of words (str).

        Returns:
          The concatenated word (str).
        """
        new_word = ""
        for i, word in enumerate(self.words):
            if i < len(word):  # Ensure the word has enough letters
                new_word += word[i]
            else:
                print(f"Ensure the word '{word}' has enough letters for their position")
        return new_word

if __name__ == '__main__':
    pass