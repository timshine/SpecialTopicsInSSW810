import unittest

"""
Author: Timothy Shine

This program has a variety of functions pertaining to strings and lists:
It can output a reversed string
It has a user defined enumerate and reverse enumerate function
It can tell if a string is a palindrome
It can find the second instance of a string in another string
Lastly, it can check if a string uses all of the characters in the alphabet
"""

def reverse(seq):
    """Takes in a string and returns a string object that is a reverse of the original string"""
    s = ''
    for i in range(len(seq)):
        s += seq[len(seq) - i - 1]
    return s

def my_enumerate(seq):
    """Generator that goes through a sequence and returns the index and value at that index starting from index 0"""
    for index in range(len(seq)):
        yield index, seq[index]

def my_reverse_enumerate(seq):
    """Generator that goes through a sequence backwards and returns the index and value at that index starting the last index"""
    rev = reverse(seq)
    for i in range(len(seq)):
        yield len(seq) - 1 - i, rev[i]

def is_palindrome(seq):
    """Takes in a string and returns true if the string is a palindrome""" 
    lower = seq.lower().replace(" " , "")   #even if there are uppercase letters or spaces it is still a palindrome by definition
    first = 0                               #first index
    last = len(lower) - 1                   #last index
    while first < last:                     #only checks halfway through for more efficient check
        if lower[first] != lower[last]:
            return False                    #short circuiting the check
        else:
            first += 1                      #moves in one closer to center
            last -= 1
    return True                             #only returns if first>last and while is over
        
def find_second(s1,s2):
    """Finds the second occurrence of s1 in s2. Will return -1 if s1 only appears once in s2, or if s1 isn't in s2 at all"""
    first = s2.find(s1)                         #finds index of first occurrence
    second = s2.find(s1, first + 1)             #searches for second occurrence starting when first occurrence ends, automatically returns -1 if none 
    return second

def remove_th(s):
    """Takes in a string s and returns a string with all words beginning or ending with 'th' removed from the input string"""
    spaceless = s.split()
    new_string = ''
    for i in spaceless:
        if len(i) < 2:
            new_string += i + ' '
        elif i[0:2].lower() == "th" or i[len(i)-2:].lower() == "th": 
            continue
        else:
            new_string += i + ' ' 
    return new_string.strip()
    
def covers_alphabet(sentence):
    """Returns true if the parameter is a string containing every letter in the alphabet
        If not, it returns false"""
    letters = "abcdefghijklmnopqrstuvwxyz"
    lower = sentence.lower()
    for i in letters:
        if i not in lower:
            return False
    return True

def main():
    print("This is my main function to test the two functions not great with unittest")
    print("Tests my_enumerate function")
    for i,v in my_enumerate("python"):
        print(i,v)

    print("Tests my_reverse_enumerate function")
    for i,v in my_reverse_enumerate("python"):
        print(i,v)
    
    print("")
    print("Now, here are my unittests")
    
    
class FractionTest (unittest.TestCase):
    def test_palindrome(self):
        """Tests if strings are palindromes"""
        self.assertTrue(is_palindrome("racecar"))                       #All lowercase
        self.assertTrue(is_palindrome("RaceCar"))                       #Some uppercase and lowercase
        self.assertTrue(is_palindrome("RaceEcar"))                      #Checks palindrome with even number of letters
        self.assertFalse(is_palindrome("abcdefg"))                      #Not a palindrome
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))   #Palindrome sentence
    
    def test_find_second(self):
        """Test find second occurrence function"""
        self.assertEqual(find_second("iss", "Mississippi"), 4)              #Tests Mississippi
        self.assertEqual(find_second("abba", "abbabba"), 3)                 #Tests when second one starts in middle of first one
        self.assertEqual(find_second("aaa", "aaaa"),1)                      #Tests another one where second starts in middle of first occurrence
        self.assertEqual(find_second("abcdefg", "This_will_never_work"),-1) #Tests when s1 isn't in s2 at all
        self.assertEqual(find_second("happy", "happybirthday"),-1)          #Tests when there is only one occurrence of s1

    def test_remove_th(self):
        """Tests function that removes any word in a string starting or ending with th"""
        self.assertEqual(remove_th("HeLLo This THat tHere tootH WoRlD"), "HeLLo WoRlD")             #Your exmaple testing upper/lower case and functionality
        self.assertEqual(remove_th("I hope that this works perfectly"), "I hope works perfectly")   #Two more fun sentences to test
        self.assertEqual(remove_th("Sentences are funny without th's in the beginning or endTH"), "Sentences are funny without in beginning or")
    
    def test_covers_alphabet(self):
        """Tests if a string has every letter in the alphabet"""
        self.assertTrue(covers_alphabet("abcdefghijklmnopqrstuvwxyz"))
        self.assertFalse(covers_alphabet("This will not have every letter"))
        self.assertTrue(covers_alphabet("aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz"))
        self.assertTrue(covers_alphabet("The quick brown fox jumps over the lazy dog"))


if __name__ == '__main__':
    main()
    unittest.main(exit=False, verbosity=2)