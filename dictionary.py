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
        return self.binsearch(0, len(self.words) - 1, word)

    def binsearch(self, l, h, word):
        while l < h:
            mid = l + (h - l)//2
            if self.words[mid] >= word:
                h = mid
            else:
                l = mid + 1
        return l

    def insertionSort(self):
        for i in range(1, len(self.words)):
            curr = self.words[i]
            idx = i
            while idx > 0 and self.words[idx - 1] > curr:
                self.words[idx] = self.words[idx - 1]
                idx -= 1
            self.words[idx] = curr

    def enhancedInsertionSort(self):
        for i in range(1, len(self.words)):
            curr = self.words[i]
            self.words.pop(i)
            idx = self.binsearch(0, i, curr)
            self.insert(curr, idx)

    def spellCheck(self, sentence):
        sentence = sentence.split()
        for i in range(len(sentence)):
            tmp = sentence[i]
            if tmp[0] in PUNC:
                tmp = tmp[1:]
            if tmp[-1] in PUNC:
                tmp = tmp[:-1]
            tmp.lower()
            check = self.binarySearch(tmp)
            if self.words[check] != tmp:
                sentence[i] = "[" + sentence[i] + "]"

        return ' '.join(sentence)

    @staticmethod
    def sortSequence(sequence):
        pass

    def anagrams(self, sequence):
        def permute(word):
            if len(word) == 0:
                return [""]

            permu = permute(word[1:])
            res = []

            for p in permu:
                for idx in range(len(p) + 1):
                    p_copy = p[:idx] + word[0] + p[idx:]
                    res.append(p_copy)
            return res

        tmp = permute(sequence)
        res = []
        for s in tmp:
            check = self.binarySearch(s)
            if self.words[check] == s:
                res.append(s)
        return res



    def crackLock(self, wheels):
        combinations = []
        res = []
        def backtrack(idx, currS):
            if len(currS) == 5:
                combinations.append(currS)
                return
            for char in wheels[idx]:
                backtrack(idx + 1, currS + char)

        backtrack(0, "")

        for combi in combinations:
            check = self.binarySearch(combi)
            if self.words[check] == combi:
                res.append(combi)

        return res



## No more testing code in this file
## To modify the testcase, go to test_dictionary.py file.

