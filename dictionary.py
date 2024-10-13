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
        if position == -1:
            self.words.append(word)
        else:
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
        while l <= h:
            mid = (l + h) // 2
            if self.words[mid] >= word:
                h = mid - 1
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
            idx = self.binsearch(0, i - 1, curr)
            self.insert(curr, idx)

    def spellCheck(self, sentence):
        sentence = sentence.split()
        res = []
        for i in range(len(sentence)):
            tmp = sentence[i]
            if tmp[0] in PUNC:
                tmp = tmp[1:]
            if tmp[-1] in PUNC:
                tmp = tmp[:-1]
            tmp.lower()
            check = self.binarySearch(tmp)
            if check >= len(self.words) or self.words[check] != tmp:
            # check = self.linearSearch(tmp)
            # if check == - 1:
                tmp = '[' + sentence[i] + ']'
            else:
                tmp = sentence[i]

            res.append(tmp)

        return ' '.join(res)

    @staticmethod
    def sortSequence(sequence):
        l = list(sequence)
        for i in range(1, len(l)):
            curr = l[i]
            idx = i
            while idx > 0 and l[idx - 1] > curr:
                l[idx] = l[idx - 1]
                idx -= 1
            l[idx] = curr
        return "".join(l)

    def anagrams(self, sequence):
        check = Dictionary.sortSequence(sequence)
        res = []

        for word in self.words:
            if Dictionary.sortSequence(word) == check:
                res.append(word)
        return res

    def crackLock(self, wheels):
        res = []

        for w in self.words:
            if len(w) == len(wheels):
                check = True
                for i in range(len(wheels)):
                    if w[i] not in wheels[i]:
                        check = False
                        break
                if check:
                    res.append(w)

        return res

## No more testing code in this file
## To modify the testcase, go to test_dictionary.py file.

