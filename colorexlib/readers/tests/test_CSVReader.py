import unittest
from colorexlib.colorexlib.readers.CSVReader import CSVReader


class TestInit(unittest.TestCase):
	def test___init__A(self):
		CSVReader("./test_website_traffic.csv", rowcol_headers=False)