import unittest
from ejercicio_1_8 import simon_says

class MyTestCase(unittest.TestCase):
    def test_simon_says(self):
        prueba_1= [1, 2]
        prueba_1b=[5, 1]
        prueba_2= [1, 2]
        prueba_2b= [5, 5]
        prueba_3= [1, 2, 3, 4, 5]
        prueba_3b= [0, 1, 2, 3, 4]
        prueba_4= [1, 2, 3, 4, 5]
        prueba_4b= [5, 5, 1, 2, 3]
        self.assertEqual(simon_says(prueba_1,prueba_1b), True)
        self.assertEqual(simon_says(prueba_2, prueba_2b), False)
        self.assertEqual(simon_says(prueba_3, prueba_3b), True)
        self.assertEqual(simon_says(prueba_4, prueba_4b), False)

if __name__ == '__main__':
    unittest.main()