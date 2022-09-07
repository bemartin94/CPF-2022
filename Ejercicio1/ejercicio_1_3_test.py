import unittest
from ejercicio_1_3 import operacion_aritmetica

class MyTestCase(unittest.TestCase):
    def test_operacion_aritmetica(self):
        prueba_1= "12 + 12"
        prueba_2= "12 - 12"
        prueba_3= "12 * 12"
        prueba_4= "12 // 0"
        self.assertEqual(operacion_aritmetica(prueba_1), 24)
        self.assertEqual(operacion_aritmetica(prueba_2), 0)
        self.assertEqual(operacion_aritmetica(prueba_3), 144)
        self.assertEqual(operacion_aritmetica(prueba_4), "No se puede dividir por 0")

if __name__ == '__main__':
    unittest.main()