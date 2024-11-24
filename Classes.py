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

if __name__ == '__main__':
    d = Dictionary()
    d.add("Banana", "A yellow fruit")
    print(d.lookup("Banana"))  # Output: A yellow fruit
    print(d.lookup("Apple"))  # Output: Word not found in the dictionary.
    sys.exit(0)