import unittest
import random

""" Author:Timothy Shine

    This program has many features
    It has the ability to count the number of vowels in a word
    It has the ability to find the last occurance of an instance in list
    It has a random number generator and the ability to find a target number by producing random numbers under a maximum amount of attempts
    Lastly, it includes a Fraction class in the form of:
    Fraction(numerator,denominator)
    and has the ability to perform functions as well as simplify the fraction"""


def count_vowels(s):
    """Counts and returns the number of vowels in a string"""
    s=s.lower()
    num_of_vowels = 0
    for letter in s:
        if letter in "aeiou":
            num_of_vowels+=1
    return num_of_vowels

def find(target,collection):
    """Finds the last occurance of a target instance in a list"""
    counter = None
    for offset, c in enumerate(collection):
        if c == target:
            counter = offset
    return counter

def random_number_gen(min,max):
    """Generator to find a random number between a minimum and a maximum range (including both the minimum and maximum numbers)"""
    while True:
        yield random.randint(min,max)
    
def find_target(target, min_value, max_value, max_attempts):
    """Returns the number of times it takes to randomly generate a number within a minimum and maximum range (including min and max)
    to find a target value. Takes in a parameter specifying the maximum attempts to find this target number using the random generator"""
    if min_value > target or max_value < target:
        raise ValueError("Target is not in min and max range")
    answer = None
    gen = random_number_gen(min_value, max_value)
    for attempt in range(max_attempts):
        if next(gen) == target:
            answer = attempt + 1
            break
    return answer 

class Fraction:
    def __init__(self, numerator, denominator):
        """Instantiates the numerator and denomintor
        This allows any Fraction object to be represented by numerator/denominator and insures only valid inputs
        Returns value error if strings are entered
        Returns zero division error if denominator is 0"""
        self.numerator = numerator
        self.denominator = denominator
        if isinstance(numerator,str) or isinstance(denominator,str):
            raise ValueError('Numerator or denominator is not a number')
        elif denominator == 0:
            raise ZeroDivisionError('Denominator cannot equal zero')
        

    def __str__(self):
        """Magic function to print the Fraction object in the form 
           numerator/denominator
           rather than printing the object location"""
        return str(self.numerator) + "/" + str(self.denominator)

    def __add__(self, other):
        """Adds the two fractions with the GCF in the denominator"""
        answer_numerator = self.numerator*other.denominator + \
            other.numerator*self.denominator
        answer_denominator = self.denominator*other.denominator
        return Fraction(answer_numerator, answer_denominator)

    def __sub__(self, other):
        """Subracts the two fractions with the GCF in the denominator"""
        answer_numerator = self.numerator*other.denominator - \
            other.numerator*self.denominator
        answer_denominator = self.denominator*other.denominator
        return Fraction(answer_numerator, answer_denominator)

    def __mul__(self, other):
        """Multiply the two fractions with the GCF in the denominator"""
        answer_numerator = self.numerator*other.numerator
        answer_denominator = self.denominator*other.denominator
        return Fraction(answer_numerator, answer_denominator)

    def __truediv__(self, other):
        """Return a fraction with the quotient of self and other where other is another fraction, returns undefined fraction object if the answer is infinity"""
        answer_numerator = self.numerator*other.denominator
        answer_denominator = self.denominator*other.numerator
        return Fraction(answer_numerator, answer_denominator)

    def __eq__(self, other):
        """Checks to see if the fractions are equal, returns true or false"""
        return self.numerator*other.denominator == self.denominator*other.numerator

    def __ne__(self, other):
        """Checks to see if the fractions are not equal, returns true or false"""
        return self.numerator*other.denominator != self.denominator*other.numerator

    def __lt__(self, other):
        """Checks to see if fraction 1 is less than fraction 2"""
        return self.numerator*other.denominator < self.denominator*other.numerator

    def __le__(self, other):
        """Checks to see if fraction 1 is less than or equal to fraction 2"""
        return self.numerator*other.denominator <= self.denominator*other.numerator

    def __gt__(self, other):
        """Checks to see if fraction 1 is greater than fraction 2"""
        return self.numerator*other.denominator > self.denominator*other.numerator

    def __ge__(self, other):
        """Checks to see if fraction 1 is greater than or equal to than fraction 2"""
        return self.numerator*other.denominator >= self.denominator*other.numerator

    def simplify(self):
        """Will simplify the fraction if it is possible"""
        gcf = 1
        if abs(self.denominator) > abs(self.numerator):
            limit = abs(self.numerator)
        else:
            limit = abs(self.denominator)
        for i in range(limit+1):
            if self.denominator % (i+1) == 0 and self.numerator % (i+1) == 0:
                gcf = i+1
        return Fraction(int(self.numerator/gcf),int(self.denominator/gcf))
       
            

class FractionTest (unittest.TestCase):
    def test_init(self):
        """verify that the numerator and denominator are set properly in the Fraction class"""
        f1 = Fraction(1, 2)
        self.assertEqual(f1.numerator, 1)
        self.assertEqual(f1.denominator, 2)

    def test_str(self):
        """ verify that __str__() method for a Fraction works properly """
        f = Fraction(3, 4)
        self.assertEqual(str(f), '3/4')

    def test_raises_exceptions(self):
        """ verify that proper exceptions are called for invalid input"""
        with self.assertRaises(ZeroDivisionError):
            Fraction(1,0)
        with self.assertRaises(ValueError):
            Fraction('abc','def')
            Fraction('abc', 2)
            Fraction('abc', 0)

    def test_plus(self):
        """ test fraction addition """
        f1 = Fraction(1, 2)
        f2 = Fraction(3, 4)
        f3 = Fraction(-5, 6)
        f4 = Fraction(-1,5)
        self.assertTrue((f1 + f1) == Fraction(4, 4)) #add itself
        self.assertTrue((f1 + f2) == Fraction(5, 4)) #add two positive fractions
        self.assertTrue((f1 + f3) == Fraction(-2,6)) #one positive one negative
        self.assertTrue((f3 + f4) == Fraction(-31,30)) #two negative

    def test_minus(self):
        """ test fraction subtraction """
        f1 = Fraction(1, 2)
        f2 = Fraction(3, 4)
        f3 = Fraction(-5, 6)
        f4 = Fraction(-1,5)
        self.assertTrue((f1 - f1) == Fraction(0, 4)) #subtract itself
        self.assertTrue((f1 - f2) == Fraction(-1, 4)) #subtract two positive fractions
        self.assertTrue((f1 - f3) == Fraction(8,6)) #subtract one positive from one negative
        self.assertTrue((f3 - f1) == Fraction(-8,6)) #subtract one negative from one positive
        self.assertTrue((f3 - f4) == Fraction(-19,30)) #subtract two negatives
    
    def test_multiply(self):
        """ test fraction multiplication """
        f1 = Fraction(1, 2)
        f2 = Fraction(3, 4)
        f3 = Fraction(-5, 6)
        f4 = Fraction(-1,5)
        self.assertTrue((f1 * f1) == Fraction(1, 4)) #multiply itself
        self.assertTrue((f1 * f2) == Fraction(3, 8)) #multiply two positive fractions
        self.assertTrue((f1 * f3) == Fraction(-5, 12)) #multiply one positive from one negative
        self.assertTrue((f3 * f4) == Fraction(5,30)) #multiply two negatives

    def test_divide(self):
        """ test fraction division """
        f1 = Fraction(1, 2)
        f2 = Fraction(3, 4)
        f3 = Fraction(-5, 6)
        f4 = Fraction(-1,5)
        self.assertTrue((f1 / f1) == Fraction(2, 2)) #divide itself
        self.assertTrue((f1 / f2) == Fraction(4, 6)) #divide two positive fractions
        self.assertTrue((f1 / f3) == Fraction(-6, 10)) #divide one positive from one negative
        self.assertTrue((f3 / f4) == Fraction(25,6)) #divide two negatives
        with self.assertRaises(ZeroDivisionError):
            Fraction (1,2) / Fraction (0,2)         #divide to cause a 0 denominator


    def test_less_than(self):
        """ test fraction less than function """
        f1 = Fraction(1, 2)
        f2 = Fraction(3, 4)
        f3 = Fraction(-5, 6)
        f4 = Fraction(-1,5)
        self.assertFalse(f1 < f1)  #it is not less than itself
        self.assertTrue(f1 < f2)   #correct less than statement
        self.assertFalse(f1 < f3)  #less than statement with one negative and one positive
        self.assertTrue(f3 < f4)   #less than statement with two negatives

    def test_less_than_equal(self):
        """ test fraction less than or equal to function """
        f1 = Fraction(1, 2)
        f2 = Fraction(3, 4)
        f3 = Fraction(-5, 6)
        f4 = Fraction(-1,5)
        self.assertTrue(f1 <= f1)  #it is less than or equal to itself
        self.assertTrue(f1 <= f2)   #correct less than or equal to statement
        self.assertFalse(f1 <= f3)  #less than or equal to statement with one negative and one positive
        self.assertTrue(f3 <= f4)   #less than or equal to statement with two negatives

    def test_greater_than_equal(self):
        """ test fraction greater than or equal to function """
        f1 = Fraction(1, 2)
        f2 = Fraction(3, 4)
        f3 = Fraction(-5, 6)
        f4 = Fraction(-1,5)
        self.assertTrue(f1 >= f1)  #it is greater than or equal to itself
        self.assertFalse(f1 >= f2)   #correct greater than or equal to statement
        self.assertTrue(f1 >= f3)  #greater than or equal to statement with one negative and one positive
        self.assertFalse(f3 >= f4)   #greater than or equal to statement with two negatives 

    def test_greater_than(self):
        """ test fraction greater than function """
        f1 = Fraction(1, 2)
        f2 = Fraction(3, 4)
        f3 = Fraction(-5, 6)
        f4 = Fraction(-1,5)
        self.assertFalse(f1 > f1)  #it is not greater than itself
        self.assertFalse(f1 > f2)   #correct greater than statement
        self.assertTrue(f1 > f3)  #greater than statement with one negative and one positive
        self.assertFalse(f3 > f4)   #greater than statement with two negatives   

    def test_not_equal(self):
        """test fraction non-equality """
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 4)
        f3 = Fraction(4, 8)
        f4 = Fraction (-1,2)
        f5 = Fraction (-2,4)
        self.assertFalse(f1 != f1) #the same fraction
        self.assertFalse(f1 != f2) #multiple of 2
        self.assertFalse(f1 != f3) #multiple of 4
        self.assertFalse(f2 != f3) #mulitple of 4
        self.assertTrue(f1 != Fraction(10, 10)) #different fractions
        self.assertTrue(f1 != f4) #same fraction but one is negative
        self.assertFalse(f4 != f5) #multiple of 2 but negative
        self.assertTrue(f4 != Fraction(-1,-2)) #one is negative one is positive
        self.assertFalse(f1 != Fraction(-1,-2)) #double negative makes a positive
    
    def test_equal(self):
        """test fraction equality """
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 4)
        f3 = Fraction(4, 8)
        f4 = Fraction (-1,2)
        f5 = Fraction (-2,4)
        self.assertTrue(f1 == f1) #the same fraction
        self.assertTrue(f1 == f2) #multiple of 2
        self.assertTrue(f1 == f3) #multiple of 4
        self.assertTrue(f2 == f3) #mulitple of 4
        self.assertFalse(f1 == Fraction(10, 10)) #different fractions
        self.assertFalse(f1 == f4) #same fraction but one is negative
        self.assertTrue(f4 == f5) #multiple of 2 but negative
        self.assertFalse(f4 == Fraction(-1,-2)) #onee is negative one is positive
        self.assertTrue(f1 == Fraction(-1,-2)) #double negative makes a positive

    def test_simplify(self):
        """tests fraction simplify"""
        self.assertEqual(str(Fraction(9,27).simplify()), str(Fraction(1,3))) #simplify fraction num<den
        self.assertEqual(str(Fraction(1,2).simplify()), str(Fraction(1,2)))  #simplify fraction in simplest
        self.assertEqual(str(Fraction(15,5).simplify()), str(Fraction(3,1))) #simplify fraction num>den
        self.assertEqual(str(Fraction(10,10).simplify()), str(Fraction(1,1))) #simplify fraction with num=den
        self.assertEqual(str(Fraction(-12,14).simplify()), str(Fraction(-6,7))) #simplify negative fraction
        self.assertEqual(str(Fraction(5,27).simplify()), str(Fraction(5,27))) #try to simplify un-simplifiable fraction            


class FindTarget (unittest.TestCase):
    def test_find(self):
        """tests find funciton when searching a list for an target"""
        self.assertEqual(find('p','apple'),2)           #checks lowercase letter in string with multiple occurances
        self.assertEqual(find(33,[42,11,23,33,4]),3)    #checks number in list of numbers
        self.assertEqual(find('x', "hello world"), None)#checks non-present letter in string
        self.assertEqual(find('a','abcdefga'),7)        #checks letter with multiple occurances
        self.assertEqual(find(0,[0,1,0,3,0,5,0]),6)     #checks number with multiple occurances
        self.assertEqual(find(0,[0,1,2,3,4,5,6]),0)     #checks boundary condition with position being 0

class CountVowelsTest (unittest.TestCase):
    def test_count_vowels(self):
        """tests count vowels function to count number of vowels in a string"""
        self.assertEqual(count_vowels('hello world'),3) #checks lowercase vowels
        self.assertEqual(count_vowels('hEllO wOrld'),3) #checks uppercase vowels
        self.assertEqual(count_vowels('hll wrld'),0)    #checks no vowels
        self.assertEqual(count_vowels('aeiou'),5)       #checks all vowels
        self.assertEqual(count_vowels(""),0)            #checks empty string

class RandomGeneratorTest (unittest.TestCase):
    """tests find target function"""
    def test_find(self):
        self.assertEqual(find_target(3,3,3,1),1)        #tests positive numbers
        with self.assertRaises(ValueError):             #tests if number is out of range
            find_target(-1,0,10,10)
        self.assertLess(find_target(2,1,2,1000),1000)   #tests a 99.9% likely solution
        self.assertEqual(find_target(1,1,1000,0),None)  #tests if no numbers are found 


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)