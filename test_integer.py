import unittest


class TestInteger(unittest.TestCase):
    def test_integer_different_value(self):
        x = 10
        y = 10
        self.assertIsNot(x,y)

    def test_integer_same_value(self):
        x = 10
        y = 20
        self.assertIs(x,y)
if __name__ == '__main__':
    unittest.main()