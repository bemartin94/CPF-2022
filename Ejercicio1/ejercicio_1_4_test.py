import unittest
from ejercicio_1_4 import check_flush

class MyTestCase(unittest.TestCase):
    def test_something1(self):
        prueba_1 = ["A_S", "J_H", "7_D", "8_D", "10_D"]
        prueba_1b = ["J_D", "3_D"]
        prueba_2 = ["10_S", "7_S", "9_H", "4_S", "3_S"]
        prueba_2b = ["K_S", "Q_S"]
        prueba_3 = ["3_S", "10_H", "10_D", "10_C", "10_S"]
        prueba_3b = ["3_S", "4_D"]

        self.assertEqual(check_flush(prueba_1, prueba_1b), True)
        self.assertEqual(check_flush(prueba_2, prueba_2b), True)
        self.assertEqual(check_flush(prueba_3, prueba_3b), False)


if __name__ == '__main__':
    unittest.main()