import unittest
from ..styling import Theme


class TestInit(unittest.TestCase):
	def test___init__A(self):
		self.assertIsInstance(
			Themes(), Themes)
