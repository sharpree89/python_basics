# TDD - Test-Driven Development
# Feature-->Write Tests-->Run & Fail-->Code-->Run & Pass-->Refactor-->Repeat

# import the python testing framework:
import unittest

# the function to be tested:
def isEven(n):
    return n % 2 == 0

# the unit tests
# initialize by creating a class that inherits from unittest.TestCase:
class IsEvenTests(unittest.TestCase):
    # each method inside the class is a test to be run on isEven()
    # failUnless() and failIf() are both methods available from unittest
    def testTwo(self):
        self.failUnless(isEven(2))

    def testThree(self):
        self.failIf(isEven(5))
        
#-------------------------------------------------------------------------------

class TruthTest(unittest.TestCase):
    # assertTrue() and assertFalse() are both methods available from unittest
    def test_assert_true(self):
        my_value = True
        self.assertTrue(my_value)

    def test_assert_false(self):
        my_value = False
        self.assertFalse(my_value)

# run the tests:
if __name__ == "__main__":
    unittest.main()
