import unittest
from collections import Counter
from collections import defaultdict

"""
Author: Timothy Shine

This program has a variety of functions pertaining to containers:
It checks if strings are anagrams using three methods: strings, default dictionaries, and containers
It checks if a string has all of the letters in the alphabet
It does a book indexing on words with corresponding page numbers
"""
def anagrams_string(s1,s2):
    """Returns True is s1 and s2 are anagrams only using strings and lists"""
    return sorted(s1.lower()) == sorted(s2.lower())

class AnagramStringTest (unittest.TestCase):
    def test_anagrams_string(self):
        """Tests if its an anagram only using the function for strings and lists"""
        self.assertTrue(anagrams_string("cinema","iceman"))
        self.assertTrue(anagrams_string("dormitory","dirtyroom"))
        self.assertTrue(anagrams_string("abcd","ABCD"))                         #capital letters shouldnt matter
        self.assertFalse(anagrams_string("ABCD","EFGH"))                        #no letters match
        self.assertFalse(anagrams_string("helloHello","hello"))                 #more letters in first word
        self.assertFalse(anagrams_string("Hi There", "Hi Hi There"))            #more letters in second word)


def anagrams_dd(s1,s2):
    """Returns True is s1 and s2 are anagrams only using default dictionaries"""
    dd = defaultdict(int)
    for char in s1.lower():
        dd[char] += 1
    for char in s2.lower():
        dd[char] -= 1
        if dd[char] == -1:
            return False                                                    #short circuiting if letter in s2 isnt in s1
    return all(0 == key for key in dd.values())

class AnagramDDTest (unittest.TestCase):
    def test_anagrams_dd(self):
        """Tests if its an anagram only using the function for default dictionaries"""
        self.assertTrue(anagrams_dd("cinema","iceman"))
        self.assertTrue(anagrams_dd("dormitory","dirtyroom"))               
        self.assertTrue(anagrams_dd("abcd","ABCD"))                         #capital letters shouldnt matter
        self.assertFalse(anagrams_dd("ABCD","EFGH"))                        #no letters match
        self.assertFalse(anagrams_dd("helloHello","hello"))                 #more letters in first word
        self.assertFalse(anagrams_dd("Hi There", "Hi Hi There"))            #more letters in second word


def anagrams_counters(s1,s2):
    """Returns True is s1 and s2 are anagrams only using counters"""
    return sorted(list(Counter(s1.lower()).most_common())) == sorted(list(Counter(s2.lower()).most_common()))  #Sorts each element in Counter and checks if the lists equal
    #or you could have return sorted(list(Counter(s1.lower()).elements())) == sorted(list(Counter(s2.lower()).elements()))

class AnagramCountersTest (unittest.TestCase):
    def test_anagrams_counters(self):
        """Tests if its an anagram only using the function counters"""
        self.assertTrue(anagrams_counters("cinema","iceman"))
        self.assertTrue(anagrams_counters("dormitory","dirtyroom"))               
        self.assertTrue(anagrams_counters("abcd","ABCD"))                         #capital letters shouldnt matter
        self.assertFalse(anagrams_counters("ABCD","EFGH"))                        #no letters match
        self.assertFalse(anagrams_counters("helloHello","hello"))                 #more letters in first word
        self.assertFalse(anagrams_counters("Hi There", "Hi Hi There"))            #more letters in second word    


def covers_alphabet(sentence):
    """Returns true if sentence inclues at least one instance of every letter in alphabet using sets"""
    return set("abcdefghijklmnopqrtsuvwxyz") <= set(sentence.lower().replace(" ",""))

class CoversAlphabetTest (unittest.TestCase):
    def test_covers_alphabet(self):
        """Tests if a string has every letter in the alphabet"""
        self.assertTrue(covers_alphabet("abcdefghijklmnopqrstuvwxyz"))
        self.assertFalse(covers_alphabet("This will not have every letter"))
        self.assertTrue(covers_alphabet("aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz"))
        self.assertTrue(covers_alphabet("The quick brown fox jumps over the lazy dog!"))               #sentence containing all letters and extra characters additional to alphabet


def book_index(words):
    """Lists all the words in the book along with the unique list of pages it appears
       Input is a list of tuples in the form ('word', page number)
       The output is a list of lists in ascending order with corresponding words and book pages"""
    dd = defaultdict(set)
    for word in sorted(words):
        dd[word[0]].add(word[1])     
    return [[key,sorted(list(value))] for key,value in dd.items()]

class TestBookIndex(unittest.TestCase):
    def test_book_index(self):
        """Tests the book index function with relatively long inputs"""
        self.assertEqual(book_index([('word1', 1), ('word2', 2), ('word1', 1), ('word1', 3)]),[['word1', [1, 3]], ['word2', [2]]])
        self.assertEqual(book_index([('how', 3), ('much', 3), ('wood', 3), ('would', 2), ('a', 1), ('woodchuck', 1), ('chuck', 3), ('if', 1), ('a', 1), ('woodchuck', 2), ('could', 2), ('chuck', 1), ('wood', 1)]),[['a', [1]], ['chuck', [1, 3]], ['could', [2]], ['how', [3]], ['if', [1]], ['much', [3]], ['wood', [1, 3]], ['woodchuck', [1, 2]], ['would', [2]]])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)