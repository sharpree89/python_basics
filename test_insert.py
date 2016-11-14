import unittest
from insert_value import insertVal

class insertValTest(unittest.TestCase):

    def setUp(self):
        self.test_list = [0,1,2,3,4]
        self.result = insertVal(2, self.test_list, 100)
        self.result2 = insertVal(8, self.test_list, 150)

    def testInsertAtIndexTwo(self):
        return self.assertEqual([0,1,100,2,3,4], self.result)

    def testReturnFalseIfOutOfRange(self):
        return self.assertEqual(False, self.result2)

if __name__ == "__main__":
    unittest.main()
