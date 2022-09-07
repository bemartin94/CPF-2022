import unittest
from ejercicio_1_1 import pluralize

class MyTestCase(unittest.TestCase):
    def test_something1(self):
        listaprueba1 = ["cow", "pig", "cow", "cow"]
        listaprueba2 = ["table", "table", "table"]
        listaprueba3 = ["chair", "pencil", "arm"]

        self.assertEqual(pluralize(listaprueba1), ['pig', 'cows'])
        self.assertEqual(pluralize(listaprueba2), ['tables'])
        self.assertEqual(pluralize(listaprueba3), ['chair', 'pencil', 'arm'])

if __name__ == '__main__':
    unittest.main()
