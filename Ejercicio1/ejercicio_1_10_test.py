import unittest
from ejercicio_1_10 import sevenBoom

class MyTestCase(unittest.TestCase):
    def test_something1(self):
        listaprueba1 = [1, 2, 3, 4, 5, 6, 7]
        listaprueba2 = [8, 6, 33, 100]
        listaprueba3 = [2, 55, 60, 97, 86]

        self.assertEqual(sevenBoom(listaprueba1), "Boom!")
        self.assertEqual(sevenBoom(listaprueba2), "No se encuentra el número 7 en el array")
        self.assertEqual(sevenBoom(listaprueba3), "Boom!")

if __name__ == '__main__':
    unittest.main()
