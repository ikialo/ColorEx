import unittest
from ..HeatMapWindow import HeatMapWindow


class TestInit(unittest.TestCase):
	def test___init__A(self):
		self.assertRaises(TypeError,HeatMapWindow)