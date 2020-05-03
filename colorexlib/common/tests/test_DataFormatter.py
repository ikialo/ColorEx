import unittest
from colorexlib.colorexlib.common.formating import DataFormatter


class TestInit(unittest.TestCase):
	def test___init__A(self):
		DataFormatter()
		DataFormatter(prefix="prefix ")
		DataFormatter(suffix="suffix")
		DataFormatter(prefix="prefix",
			suffix="suffix")
		DataFormatter(format_strings=
			['.2f'])

	def test___init__B(self):
		self.assertRaises(TypeError,
			DataFormatter, prefix=872)
		self.assertRaises(TypeError,
			DataFormatter, prefix=list())
		self.assertRaises(TypeError,
			DataFormatter, prefix=dict())
		self.assertRaises(TypeError,
			DataFormatter, prefix=89.123)


	def test___init__C(self):
		self.assertRaises(TypeError,
			DataFormatter, suffix=872)
		self.assertRaises(TypeError,
			DataFormatter, suffix=list())
		self.assertRaises(TypeError,
			DataFormatter, suffix=dict())
		self.assertRaises(TypeError,
			DataFormatter, suffix=89.123)


	def test___init__D(self):
		self.assertRaises(TypeError,
			DataFormatter, format_strings=872)
		self.assertRaises(TypeError,
			DataFormatter, format_strings=[4,5,2])
		self.assertRaises(TypeError,
			DataFormatter, format_strings=dict())
		self.assertRaises(TypeError,
			DataFormatter, format_strings=89.123)



class TestFormat(unittest.TestCase):

	def setUp(self):
		self.d1 = DataFormatter(suffix=" "+chr(177)+"C",
			format_strings=['.2f'])
		self.d2 = DataFormatter(prefix="$ ",
			format_strings=['.2f'])



	def test_format_A(self):
		self.assertEqual(self.d1.format(78.2922),
			"78.29 "+chr(177)+"C")
		self.assertEqual(self.d1.format(108.499),
			"108.50 "+chr(177)+"C")
		self.assertEqual(self.d1.format(80.555),
			"80.56 "+chr(177)+"C")
		self.assertEqual(self.d1.format(25),
			"25.00 "+chr(177)+"C")


	def test_format_B(self):
		self.assertEqual(self.d2.format(-78.2922),
			"$ -78.29")
		self.assertEqual(self.d2.format(108.499),
			"$ 108.50")
		self.assertEqual(self.d2.format(80.555),
			"$ 80.56")
		self.assertEqual(self.d2.format(25),
			"$ 25.00")















