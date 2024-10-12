"""
ECE241 - Fall 2024
Project 1 - Dictionary
Fill in your code in this file!
"""
import random ## NO MORE PACKAGE. ADDITION IMPORT STATEMENT WILL FAIL THE AUTOGRADER

PUNC =  "’!()-[]{};:’\"\,<>./?@#$%^&*_~’" # this is a constant that you might use in this project.

class Dictionary:
    def __init__(self):
        self.words = []  # store all your words here

    def insert(self, word, position = -1):
        self.words.insert(position, word)

    def shuffle(self):
        random.shuffle(self.words)

    def loadFromFile(self, filename):
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                self.words.append(line)

    def linearSearch(self, word):
        for i in range(len(self.words)):
            if self.words[i] == word:
                return i
        return -1

    def binarySearch(self, word):
        def binsearch (l, h, word):
            while l < h:
                mid = l + (h - l)//2
                if self.words[mid] >= word:
                    h = mid
                else:
                    l = mid + 1
            return l
        return binsearch(0, len(self.words) - 1, word)

    def insertionSort(self):
        n = len(self.words)

        for i in range(1, n):
            curr = self.words[i]
            idx = i
            while idx > 0 and self.words[idx - 1] > curr:
                self.words[idx] = self.words[idx - 1]
                idx -= 1
            self.words[idx] = curr

    def enhancedInsertionSort(self):


    def spellCheck(self, sentence):
        pass

    @staticmethod
    def sortSequence(sequence):
        pass

    def anagrams(self, sequence):
        pass

    def crackLock(self, wheels):
        pass


## No more testing code in this file
## To modify the testcase, go to test_dictionary.py file.

