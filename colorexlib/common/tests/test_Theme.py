import unittest
from colorexlib.colorexlib.common.styling import Theme


class TestInit(unittest.TestCase):
	def test___init__A(self):
		t = Theme(primaryColor="#ffffff")
		self.assertIsInstance(
			Theme(), Theme)

	def test___init__B(self):
		t = Theme()


	def test___init__C(self):
		t = Theme(primaryColor="red")


	def test___init__D(self):
		t = Theme(primaryColor="red",
			secondaryColor="#ff00aa")


	def test___init__E(self):
		t = Theme(primaryColor="red",
			secondaryColor="blue",
			onPrimaryColor="olive")

	def test___init__F(self):
		t = Theme(primaryColor="red",
			secondaryColor="#00aa11",
			onPrimaryColor="black",
			onSecondaryColor="#89a762")


	def test___init__G(self):
		t = Theme(primaryColor="red",
			secondaryColor="#00aa11",
			onPrimaryColor="black",
			onSecondaryColor="#89a762",
			backgroundColor="#45aacc")


	def test___init__H(self):
		t = Theme(primaryColor="red",
			secondaryColor="#00aa11",
			onPrimaryColor="black",
			onSecondaryColor="#89a762",
			backgroundColor="#45aacc",
			onBackgroundColor="yellow")


	def test___init__I(self):
		self.assertRaises(TypeError,
			Theme,primaryColor="#ffffff0")



	def test___init__I(self):
		self.assertRaises(TypeError,
			Theme,primaryColor="lightyellow",
			secondaryColor="#45aa99")


	def test___init__J(self):
		self.assertRaises(TypeError,
			Theme,primaryColor="black",
			secondaryColor="#45aa99",
			backgroundColor="blue",
			onBackgroundColor="#45kkaa")


	def test___init__K(self):
		self.assertRaises(TypeError,
			Theme,primaryColor="black",
			secondaryColor="#45aa99",
			backgroundColor="blue",
			onBackgroundColor="pink",
			onPrimaryColor="#lmno44")


	def test___init__K(self):
		self.assertRaises(TypeError,
			Theme,primaryColor="black",
			secondaryColor="#45aa99",
			backgroundColor="blue",
			onBackgroundColor=908,
			onPrimaryColor="#lmno44")


	def test___init__M(self):
		self.assertRaises(TypeError,
			Theme,primaryColor="black",
			secondaryColor="#45aa99",
			backgroundColor="blue",
			onBackgroundColor="ffffff",
			onPrimaryColor="#aaaaaa")









class TestPalette(unittest.TestCase):
	def test_palette_A(self):
		self.assertIsInstance(
			Theme().palette,dict)

	def test_palette_B(self):
		total_keys = 6
		self.assertEqual(
			len(Theme().palette.keys()),
				total_keys)


	def test_palette_C(self):
		keys = [
			'primary',
			'secondary',
			'on-primary',
			'on-secondary',
			'background',
			'on-background'
		]
		theme = Theme()
		for key in keys:
			self.assertTrue(
				key in theme.palette.keys()
		)


