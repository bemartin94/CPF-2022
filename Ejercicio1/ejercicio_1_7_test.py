import unittest
from ejercicio_1_7 import unique_sort

class MyTestCase(unittest.TestCase):
    def test_something1(self):
        listaprueba1 = [1, 2, 4, 3]
        listaprueba2 = [1, 4, 4, 4, 4, 4, 3, 2, 1, 2]
        listaprueba3 = [6, 7, 3, 2, 1]

        self.assertEqual(unique_sort(listaprueba1),  [1, 2, 3, 4])
        self.assertEqual(unique_sort(listaprueba2),  [1, 2, 3, 4])
        self.assertEqual(unique_sort(listaprueba3), [1, 2, 3, 6, 7])

if __name__ == '__main__':
    unittest.main()
