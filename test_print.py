import unittest
from Hello import *

class Test_print(unittest.TestCase):
  def test_print(self):
    self.assertEqual(name(),"Hello aditi!!")
    self.assertEqual(name1(), "Hello Ashmitha!!")
    
if __name__ == '__main__':
    unittest.main()
