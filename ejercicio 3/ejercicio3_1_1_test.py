import unittest
from ejercicio3_1_1 import Rectangulo

class Ejercicio1TestCase(unittest.TestCase):
    def test_area_5base_2altura_10(self):
        rectangulo = Rectangulo(base=5,altura=2)
        area = rectangulo.calcular_area()
        self.assertEqual(area, 10)

    def test_perimetro_5base_2altura_14(self):
        rectangulo = Rectangulo(base=5,altura=2)
        perimetro = rectangulo.calcular_perimetro()
        self.assertEqual(perimetro, 14)

if __name__ == '__main__':
    unittest.main()