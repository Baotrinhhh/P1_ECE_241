"""
ECE241 - Fall 2024
Project 1 - Dictionary
Fill in your code in this file!
"""
import random  # NO MORE PACKAGE. ADDITION IMPORT STATEMENT WILL FAIL THE AUTOGRADER

PUNC = "’!()-[]{};:’\"\,<>./?@#$%^&*_~’"  # this is a constant that you might use in this project.


class Dictionary:
    """
    A class used to represent a Dictionary.

    Attributes
    ----------
    words : list
        a list to store all words in the dictionary

    Methods
    -------
    insert(word, position=-1):
        Inserts a word into the dictionary at the specified position.
    shuffle():
        Shuffles the words in the dictionary.
    loadFromFile(filename):
        Loads words from a file into the dictionary.
    linearSearch(word):
        Searches for a word using linear search.
    binarySearch(word):
        Searches for a word using binary search.
    binsearch(l, h, word):
        Helper method for binary search.
    insertionSort():
        Sorts the words in the dictionary using insertion sort.
    enhancedInsertionSort():
        Sorts the words in the dictionary using an enhanced insertion sort.
    spellCheck(sentence):
        Checks the spelling of words in a sentence.
    sortSequence(sequence):
        Sorts the characters in a sequence.
    anagrams(sequence):
        Finds anagrams of a given sequence in the dictionary.
    crackLock(wheels):
        Finds possible combinations from a set of wheels.
    """

    def __init__(self):
        """
        Initializes the Dictionary with an empty list of words.

        :return: None
        """
        self.words = []  # store all words here

    def insert(self, word, position=-1):
        """
        Inserts a word into the dictionary at the specified position.

        :param word: The word to be inserted.
        :param position: The position at which to insert the word (default is -1, which appends the word).
        :return: None
        """
        if position == -1:
            self.words.append(word)  # append word if position is -1 (no position specified)
        else:
            self.words.insert(position, word)  # insert word at the specified position

    def shuffle(self):
        """
        Shuffles the words in the dictionary.

        :return: None
        """
        random.shuffle(self.words)  # shuffle the list of words

    def loadFromFile(self, filename):
        """
        Loads words from a file into the dictionary.

        :param filename: The name of the file to load words from.
        :return: None
        """
        with open(filename, "r") as file: # open file in read mode
            for line in file:
                line = line.strip()  # remove leading/trailing whitespace
                self.words.append(line)  # add word to the list

    def linearSearch(self, word):
        """
        Searches for a word using linear search.

        :param word: The word to search for.
        :return: int - The index of the word if found, otherwise -1.
        """
        for i in range(len(self.words)):
            if self.words[i] == word:  # check if current word matches the search word
                return i  # return index if found
        return -1  # return -1 if not found

    def binarySearch(self, word):
        """
        Searches for a word using binary search.

        :param word: The word to search for.
        :return: int - The index where the word should be if found, otherwise the insertion point.
        """
        return self.binsearch(0, len(self.words) - 1, word)  # call helper method for binary search

    def binsearch(self, l, h, word):
        """
        Helper method for binary search.

        :param l: The lower bound of the search range.
        :param h: The upper bound of the search range.
        :param word: The word to search for.
        :return: int - The index where the word should be if found, otherwise the insertion point.
        """
        while l <= h:
            mid = (l + h) // 2  # calculate mid-point
            if self.words[mid] >= word: # check if mid-point word is greater than or equal to search word
                h = mid - 1  # adjust upper bound
            else:
                l = mid + 1  # adjust lower bound
        return l  # return insertion point

    def insertionSort(self):
        """
        Sorts the words in the dictionary using insertion sort.

        :return: None
        """
        for i in range(1, len(self.words)):
            curr = self.words[i]  # current word to be inserted
            idx = i
            while idx > 0 and self.words[idx - 1] > curr:
                self.words[idx] = self.words[idx - 1]  # shift larger words to the right
                idx -= 1
            self.words[idx] = curr  # insert current word at the correct position

    def enhancedInsertionSort(self):
        """
        Sorts the words in the dictionary using an enhanced insertion sort.

        :return: None
        """
        for i in range(1, len(self.words)):
            curr = self.words[i]  # current word to be inserted
            self.words.pop(i)  # remove current word from the list
            idx = self.binsearch(0, i - 1, curr)  # find the correct position using binary search
            self.insert(curr, idx)  # insert current word at the correct position

    def spellCheck(self, sentence):
        """
        Checks the spelling of words in a sentence.

        :param sentence: The sentence to check.
        :return: str - The sentence with misspelled words enclosed in square brackets.
        """
        sentence = sentence.split()  # split sentence into words
        res = []
        for i in range(len(sentence)):
            tmp = sentence[i]
            if tmp[0] in PUNC:
                tmp = tmp[1:]  # remove leading punctuation
            if tmp[-1] in PUNC:
                tmp = tmp[:-1]  # remove trailing punctuation
            tmp.lower()  # convert to lowercase
            check = self.binarySearch(tmp)  # check spelling using binary search
            if check >= len(self.words) or self.words[check] != tmp:
                tmp = '[' + sentence[i] + ']'  # mark misspelled word
            else:
                tmp = sentence[i]

            res.append(tmp)
        return ' '.join(res)  # join words back into a sentence

    @staticmethod
    def sortSequence(sequence):
        """
        Sorts the characters in a sequence.

        :param sequence: The sequence to sort.
        :return: str - The sorted sequence.
        """
        l = list(sequence)  # convert sequence to list of characters
        for i in range(1, len(l)):
            curr = l[i]  # current character to be inserted
            idx = i
            while idx > 0 and l[idx - 1] > curr:
                l[idx] = l[idx - 1]  # shift larger characters to the right
                idx -= 1
            l[idx] = curr  # insert current character at the correct position
        return "".join(l)  # convert list back to string

    def anagrams(self, sequence):
        """
        Finds anagrams of a given sequence in the dictionary.

        :param sequence: The sequence to find anagrams for.
        :return: list - A list of anagrams found in the dictionary.
        """
        check = Dictionary.sortSequence(sequence)  # sort the sequence
        res = []

        for word in self.words:
            if Dictionary.sortSequence(word) == check:  # check if sorted word matches sorted sequence
                res.append(word)  # add word to the result list
        return res

    def crackLock(self, wheels):
        """
        Finds possible combinations from a set of wheels.

        :param wheels: list of list of str - The wheels to find combinations from.
        :return: list - A list of possible combinations found in the dictionary.
        """
        res = []

        for w in self.words:
            if len(w) == len(wheels):  # check if word length matches number of wheels
                check = True
                for i in range(len(wheels)):
                    if w[i] not in wheels[i]:  # check if character is in the corresponding wheel
                        check = False
                        break
                if check:
                    res.append(w)  # add word to the result list

        return res

# No more testing code in this file
# To modify the testcase, go to test_dictionary.py file.