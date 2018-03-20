import unittest

"""
Author: Timothy Shine

This program has a variety of functions pertaining to manipulating lists:
It can count the number of occurrences of distinct values in a list.
It can return a copy of a string with the vowels removed
And it can sort a sequence of numbers or letters using an insert sort
"""

def distinct_values(s):
    """Counts the number of distinct values in a list and returns the value with the number of occurrences as a new list"""
    values = list()
    for char in s:                                              #List of unique values
        if char not in values:
            values.append(char)
    value_number = [[char, s.count(char)] for char in values]   #List comprehension to return list of values and number of occurrences
    return value_number

class DistinctValueTest (unittest.TestCase):
    def test_distinct_values(self):
        """Tests distinct_values function using letters and numbers"""
        self.assertEqual(distinct_values("Mississippi"), [['M', 1], ['i', 4], ['s', 4], ['p', 2]])
        self.assertEqual(distinct_values([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]), [[1, 1], [2, 2], [3, 3], [4, 4]])

def remove_vowels(s):
    """Returns a copy of string s with no vowels"""
    return ''.join([char for char in s.lower() if char not in 'aeiou']) #joins list of characters back into a string

class RemoveVowelTest (unittest.TestCase):
    """Tests remove_vowels function"""
    def test_remove_vowels(self):
        self.assertEqual(remove_vowels("hello world"), "hll wrld")
        self.assertEqual(remove_vowels("Is the number 2 a vowel?"), "s th nmbr 2  vwl?")


def insert_sort(seq):
    """Returns a copy of the argument sorted using a list and the insertion algorithm"""
    sort = list()                               #creates an empty sorted list
    for i in seq:                               #iterates from the first item of the list to the end of the list
        for offset, value in enumerate(sort):   #iterates through the sorted list from left to right
            if i <= value:                      #if new value is less than value at index of the sorted list, insert the new value at that index
                sort.insert(offset, i)
                break
        else:
            sort.append(i)                      #if the value wasn't smaller than any values in the list, append it to the end
    return sort       

class InsertSortTest (unittest.TestCase):
    """Tests insertion sort funciton with numbers and letters"""
    def test_insert_sort(self):
        self.assertEqual(insert_sort([1, 5, 3, 3]), [1, 3, 3, 5])
        self.assertEqual(insert_sort([1, 3, 4, 7, 8, 2, 5, 6, 9, 0]), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(insert_sort(['a', 'c', 'd', 'b']), ['a', 'b', 'c', 'd'])
        self.assertEqual(insert_sort([0, 1, 0.2, 0.8, 0.6, 0.4]), [0, 0.2, 0.4, 0.6, 0.8, 1])
        self.assertEqual(insert_sort([]),[])

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)