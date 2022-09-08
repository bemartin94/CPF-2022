import unittest
from ejercicio_1_11 import letrasMultiplicadas


class MyTestCase(unittest.TestCase):
    def test_something1(self):
        prueba_1 = "AAA"
        prueba_2 = "AAAAAFFFFOOOA"
        prueba_3 = "111223333344"
        prueba_4 = "AABB"

        self.assertEqual(letrasMultiplicadas(prueba_1, 2), "AA")
        self.assertEqual(letrasMultiplicadas(prueba_2, 2), "AAFFOOA")
        self.assertEqual(letrasMultiplicadas(prueba_3, 1), "1234")
        self.assertEqual(letrasMultiplicadas(prueba_4, 1), "AB")


if __name__ == '__main__':
    unittest.main()
