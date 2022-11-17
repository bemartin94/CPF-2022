import unittest
from ejercicio_1_12 import combinaciones


class MyTestCase(unittest.TestCase):
    def test_something1(self):
        prueba_1 = ['a', 'b', 'c']

        self.assertEqual(combinaciones(prueba_1, 7), "aa ab ac ba bb bc ca cb cc")

if __name__ == '__main__':
    unittest.main()
