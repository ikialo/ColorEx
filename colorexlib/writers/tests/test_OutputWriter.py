import unittest
from colorexlib.colorexlib.writers.OutputWriter import OutputWriter

class TestInit(unittest.TestCase):
	def test_init_A(self):
		self.assertRaises(TypeError,
			OutputWriter)
