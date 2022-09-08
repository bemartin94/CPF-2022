import unittest
from ejercicio_1_6 import square_digits

class MyTestCase(unittest.TestCase):
    def test_something1(self):

        self.assertEqual(square_digits(9119), 811181)
        self.assertEqual(square_digits(2483), 416649)
        self.assertEqual(square_digits(3212), 9414)

if __name__ == '__main__':
    unittest.main()
