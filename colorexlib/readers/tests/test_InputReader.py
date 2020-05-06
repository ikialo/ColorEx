import unittest
from colorexlib.colorexlib.readers.InputReader import InputReader


class TestInit(unittest.TestCase):
	def test_init_A(self):
		self.assertRaises(TypeError,
			InputReader)
