import unittest
from Hello import *

class Test_print(unittest.TestCase):
  def test_print(self):
    self.assertEqual(print(),"Hello aditi!!")
