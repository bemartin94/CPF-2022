import unittest
from ejercicio_1_2 import same_length

class MyTestCase(unittest.TestCase):
    def test_something1(self):
        stringprueba1 = "110011100010"
        stringprueba2 = "101010110"
        stringprueba3 = "111100001100"
        stringprueba4 = "111"

        self.assertEqual(same_length(stringprueba1), True)
        self.assertEqual(same_length(stringprueba2), False)
        self.assertEqual(same_length(stringprueba3), True)
        self.assertEqual(same_length(stringprueba4), False)


if __name__ == '__main__':
    unittest.main()