import unittest
from ..formatting import DataFormatter


class TestInit(unittest.TestCase):
	def test___init__A(self):
		DataFormatter()
		DataFormatter(prefix="prefix ")
		DataFormatter(suffix="suffix")
		DataFormatter(prefix="prefix",
			suffix="suffix")
		DataFormatter(format_strings=
			['.2f'])