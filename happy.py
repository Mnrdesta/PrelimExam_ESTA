import unittest

class Test(unittest.TestCase):
    def testAssert(self):
        result = "HAPPY"
        self.assertEqual(result, "SAD")

if __name__ == '__main__':
    unittest.main()