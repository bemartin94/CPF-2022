import unittest
from ejercicio_1_9 import get_budgets

class MyTestCase(unittest.TestCase):
    def test_operacion_aritmetica(self):
        prueba_1= [
  { "name": "John", "age": 21, "budget": 23000 },
  { "name": "Steve",  "age": 32, "budget": 40000 },
  { "name": "Martin",  "age": 16, "budget": 2700 }
]
        prueba_2= [
  { "name": "John",  "age": 21, "budget": 29000 },
  { "name": "Steve",  "age": 32, "budget": 32000 },
  { "name": "Martin",  "age": 16, "budget": 1600 }
]
        self.assertEqual(get_budgets(prueba_1), 65700)
        self.assertEqual(get_budgets(prueba_2), 62600)

if __name__ == '__main__':
    unittest.main()