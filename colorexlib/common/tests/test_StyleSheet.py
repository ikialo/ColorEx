import unittest
from ..styling import StyleSheet


class TestInit(unittest.TestCase):
	def test___init__A(self):
		s1 = StyleSheet()
		s2 = StyleSheet(tile_size=(80,100))
		s3 = StyleSheet(title_ycoord=50)
		s4 = StyleSheet(axes_tick_length=100)
		s5 = StyleSheet(axes_label_bold=True,
			tile_size=(10,10))
	def test___init__B(self):
		self.assertRaises(TypeError,
			StyleSheet,tile_size=80
		)
		self.assertRaises(TypeError,
			StyleSheet,axes_tick_length=[1,2,3])
		self.assertRaises(TypeError,
			StyleSheet,axes_label_size="eleven")
		self.assertRaises(TypeError,
			StyleSheet,"parameter")
		self.assertRaises(TypeError,
			StyleSheet,title_font=133)
		self.assertRaises(TypeError,
			StyleSheet,
			canvas_size_factor=205.5)
		self.assertRaises(TypeError,
			StyleSheet,
			plane_top_margin=20,
			xlabel_margin="twenty")


class TestStyles(unittest.TestCase):
	def test_styles_A(self):
		self.assertIsInstance(StyleSheet().styles,
			dict)
	def test_styles_B(self):
		stylesheet = StyleSheet()
		keys = [
			'tile_size','plane_top_margin','canvas_size_factor',
			'canvas_top_margin','canvas_bottom_margin',
			'ylabel_margin','xlabel_margin','axes_title_font',
			'axes_title_size','axes_title_bold','axes_tick_length',
			'axes_label_font','axes_label_size','axes_label_bold',
			'title_font','title_size','title_bold','title_ycoord',
			'subtitle_font','subtitle_size','subtitle_bold','subtitle_ycoord'
		]


		self.assertEqual(len(stylesheet.styles.keys()),
			len(keys))

		for key in keys:
			self.assertTrue(key in stylesheet.styles.keys())

	def test_styles_C(self):
		s1 = StyleSheet(canvas_size_factor=0.24)
		self.assertEqual(s1.styles['canvas_size_factor'],
			0.24)
	def test_styles_D(self):
		s1 = StyleSheet(axes_label_size=56)
		self.assertEqual(s1.styles['axes_label_size'],
			56)
	def test_styles_E(self):
		s1 = StyleSheet(title_font="Arial")
		self.assertEqual(s1.styles['title_font'],
			"Arial")

	def test_styles_F(self):
		s1 = StyleSheet(axes_label_bold=True)
		self.assertEqual(s1.styles['axes_label_bold'],
			True)