from dictionary import Dictionary
import string

def is_sorted(alist):
    for i in range(len(alist)-1):
        if alist[i] > alist[i+1]:
            return False

    return True

if __name__ == "__main__":
    dic = Dictionary()
    print("Test 1.1: inserting word ``hello'' into the dictionary")
    dic.insert("hello")
    print("After insertion, the dictionary is", dic.words)
    # Excepted: After insertion, the dictionary is ['hello']
    print("Test 1.2: inserting word ``world'' into the dictionary at position 0")
    dic.insert("world", 0)
    print("After insertion, the dictionary is", dic.words)
    # Excepted: After insertion, the dictionary is ['world', 'hello']
    # Insert AAAA to AAAZ to the dictionary
    for c in string.ascii_letters:
        dic.insert("AAA" + c.upper())

    print("Test 2: shuffle the dictionary")
    print("Before shuffle, the first three word in the dictionary is", dic.words[:3])
    dic.shuffle()
    print("After shuffle, the first three word in the dictionary is", dic.words[:3])
    # You should except something other than ['world', 'hello', 'AAAA']

    dic = Dictionary()
    print("Test 3: load from file")
    dic.loadFromFile("short.txt")
    print("The first three words in the dictionary are", dic.words[:3])
    # Excepted: ['simon', 'electrical', 'ate']
    print("Task 4.1: searching for word ``school'' with linear search")
    index = dic.linearSearch("school")
    print("The index for word ``school'' is", index)
    # Excepted 9
    print("Test 4.2: searching for word ``systemwow64'' with linear search")
    index = dic.linearSearch("systemwow64")
    print("The index for word ``systemwow64'' is", index)
    # Excepted: -1

    dic.words.sort() # NOTE: YOU ARE NOT ALLOWED TO DO SO IN THE CODE FILE.

    print("Test 5.1: search for word ``school'' with binary search")
    index = dic.binarySearch("school")
    print("The index for word ``school'' is", index)
    # Excepted: 14. Note, this is the position after the dictionary is sorted, therefore, different from the previous
    # linear search, 9
    print("Test 5.2: search for word ``systemwow64'' with binary search")
    index = dic.binarySearch("systemwow64")
    print("The index for word ``systemwow64'' is", index)
    # Excepted: 18

    dic.shuffle()
    print("Test 6: insertion sort")
    if is_sorted(dic.words):
        print("THIS WILL NEVER HAPPEN, IF YOU SAW THIS MESSAGE, CHECK YOUR SHUFFLE METHOD")
    else:
        print("Before insertion sort, the array is unsorted")

    dic.insertionSort()
    if is_sorted(dic.words):
        print("After insertion sort, the array is sorted")
    else:
        print("Your insertion sort does not fully sort the array")

    print("Test 7: enhanced insertion sort")
    dic.shuffle()
    if is_sorted(dic.words):
        print("THIS WILL NEVER HAPPEN, IF YOU SAW THIS MESSAGE, CHECK YOUR SHUFFLE METHOD")
    else:
        print("Before enhanced insertion sort, the array is unsorted")

    dic.enhancedInsertionSort()
    if is_sorted(dic.words):
        print("After enhanced insertion sort, the array is sorted")
    else:
        print("Your enhanced insertion sort does not fully sort the array")

    print("Test 8: Spell check")
    sentence = "Does cat eat dog?"
    sc = dic.spellCheck(sentence)
    print("After spell check, the sentence is ``" + sc + "''")
    # Excepted: [Does] cat eat [dog?]

    print("Test 9: get anagrams")
    sequence = 'tae'
    anagrams = dic.anagrams(sequence)
    print("Anagrams", anagrams)
    # Excepted: ['ate', 'eat', 'tea']
    wheels = [
        ['x', 'y', 'c', 's'],
        ['a', 'l', 'i', 'm'],
        ['o', 'm', 's', 'a'],
        ['o', 'x', 'a', 's'],
        ['s', 'm', 'n', 'q']
    ]
    print("Test 10: crack lock")
    combs = dic.crackLock(wheels)
    print("Combinations", combs)
    # Excepted: ['class', 'simon']
