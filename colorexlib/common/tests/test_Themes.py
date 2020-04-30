import unittest
from ..styling import Themes


class TestInit(unittest.TestCase):
	def test___init__A(self):
		self.assertIsInstance(
			Themes(), Themes)






class TestThemes(unittest.TestCase):
	def test_themes_A(self):
		self.assertIsInstance(
			Themes().themes, dict)
	def test_themes_B(self):
		themes = dict()
		default = dict()
		default['primary'] = '#0044aa'
		default['secondary'] = '#aaccff'
		default['on-primary'] = '#d7eef4'
		default['on-secondary'] = '#f9f9f9'
		sun = dict()
		sun['primary'] = '#d45500'
		sun['secondary'] = '#ffccaa'
		sun['on-primary'] = '#ffccaa'
		sun['on-secondary'] = '#000000'
		themes['default'] = default
		themes['sun'] = sun
		self.assertEqual(Themes().themes,
        	themes)





class TestColors(unittest.TestCase):
	def test_colors_A(self):
		self.assertIsInstance(
			Themes().colors, dict)
	def test_colors_B(self):
		colors = dict()
		colors['default'] = '#000000'
		colors['black'] = '#000000'
		colors['white'] = '#ffffff'
		colors['red'] = '#ff0000'
		colors['lime'] = '#00ff00'
		colors['blue'] = '#0000ff'
		colors['yellow'] = '#ffff00'
		colors['cyan'] = '#00ffff'
		colors['aqua'] = '#00ffff'
		colors['magenta'] = '#ff00ff'
		colors['fuchsia'] = '#ff00ff'
		colors['silver'] = '#c0c0c0'
		colors['gray'] = '#808080'
		colors['grey'] = '#808080'
		colors['maroon'] = '#800000'
		colors['olive'] = '#808000'
		colors['green'] = '#008000'
		colors['purple'] = '#800080'
		colors['teal'] = '#008080'
		colors['navy'] = '#000080'
		self.assertEqual(Themes().colors,
			colors)





class TestIsRgbHex(unittest.TestCase):
	def test_is_rgb_hex_A(self):
		test_rgb_hex = '#4411aa'
		self.assertTrue(
			Themes().is_rgb_hex(test_rgb_hex))
	def test_is_rgb_hex_B(self):
		test_rgb_hex = '#4411bb'
		self.assertTrue(
			Themes().is_rgb_hex(test_rgb_hex))
	def test_is_rgb_hex_C(self):
		test_rgb_hex = '#1c1caa'
		self.assertTrue(
			Themes().is_rgb_hex(test_rgb_hex))
	def test_is_rgb_hex_D(self):
		test_rgb_hex = '#f190ac'
		self.assertTrue(
			Themes().is_rgb_hex(test_rgb_hex))
	def test_is_rgb_hex_E(self):
		test_rgb_hex = '#45acbb'
		self.assertTrue(
			Themes().is_rgb_hex(test_rgb_hex))
	def test_is_rgb_hex_F(self):
		test_rgb_hex = 'color1'
		self.assertFalse(
			Themes().is_rgb_hex(test_rgb_hex))
	def test_is_rgb_hex_G(self):
		test_rgb_hex = '9018'
		self.assertFalse(
			Themes().is_rgb_hex(test_rgb_hex))
	def test_is_rgb_hex_H(self):
		test_rgb_hex = 2016
		self.assertFalse(
			Themes().is_rgb_hex(test_rgb_hex))
	def test_is_rgb_hex_I(self):
		test_rgb_hex = 'ff00aa'
		self.assertFalse(
			Themes().is_rgb_hex(test_rgb_hex))
	def test_is_rgb_hex_J(self):
		test_rgb_hex = '#ffaabb00'
		self.assertFalse(
			Themes().is_rgb_hex(test_rgb_hex))
	def test_is_rgb_hex_K(self):
		test_rgb_hex = '#hh11ff'
		self.assertFalse(
			Themes().is_rgb_hex(test_rgb_hex))






class TestIsRgbDecimal(unittest.TestCase):
	def test_is_rgb_decimal_A(self):
		test_dec_color = (201,55,20)
		self.assertTrue(
			Themes().is_rgb_decimal(test_dec_color))
	def test_is_rgb_decimal_B(self):
		test_dec_color = (201,55,255)
		self.assertTrue(
			Themes().is_rgb_decimal(test_dec_color))
	def test_is_rgb_decimal_C(self):
		test_dec_color = (10,10,200)
		self.assertTrue(
			Themes().is_rgb_decimal(test_dec_color))
	def test_is_rgb_decimal_D(self):
		test_dec_color = (0,55,0)
		self.assertTrue(
			Themes().is_rgb_decimal(test_dec_color))
	def test_is_rgb_decimal_E(self):
		test_dec_color = ('56',25,11)
		self.assertFalse(
			Themes().is_rgb_decimal(test_dec_color))
	def test_is_rgb_decimal_F(self):
		test_dec_color = (256,11,20)
		self.assertFalse(
			Themes().is_rgb_decimal(test_dec_color))
	def test_is_rgb_decimal_G(self):
		test_dec_color = (20,299,20)
		self.assertFalse(
			Themes().is_rgb_decimal(test_dec_color))
	def test_is_rgb_decimal_H(self):
		test_dec_color = (1,0,289)
		self.assertFalse(
			Themes().is_rgb_decimal(test_dec_color))
	def test_is_rgb_decimal_I(self):
		test_dec_color = "#ff00aa"
		self.assertFalse(
			Themes().is_rgb_decimal(test_dec_color))




class TestRgbHexToDecimal(unittest.TestCase):
	def test_rgb_hex_to_decimal_A(self):
		rgb_hex = "#ff00aa"
		rgb_dec = (255,0,170)
		self.assertEqual(
			Themes().rgb_hex_to_decimal(
				rgb_hex), rgb_dec)
	def test_rgb_hex_to_decimal_B(self):
		rgb_hex = "#0ac123"
		rgb_dec = (10,193,35)
		self.assertEqual(
			Themes().rgb_hex_to_decimal(
				rgb_hex), rgb_dec)
	def test_rgb_hex_to_decimal_C(self):
		rgb_hex = "#ffffff"
		rgb_dec = (255,255,255)
		self.assertEqual(
			Themes().rgb_hex_to_decimal(
				rgb_hex), rgb_dec)
	def test_rgb_hex_to_decimal_D(self):
		rgb_hex = "#aa44ab"
		rgb_dec = (170,68,171)
		self.assertEqual(
			Themes().rgb_hex_to_decimal(
				rgb_hex), rgb_dec)
	def test_rgb_hex_to_decimal_E(self):
		rgb_hex = "#aa44abc"
		self.assertRaises(TypeError,
			Themes().rgb_hex_to_decimal,
			rgb_hex)
	def test_rgb_hex_to_decimal_F(self):
		rgb_hex = "aa44ff"
		self.assertRaises(TypeError,
			Themes().rgb_hex_to_decimal,
			rgb_hex)
	def test_rgb_hex_to_decimal_G(self):
		rgb_hex = "blue"
		self.assertRaises(TypeError,
			Themes().rgb_hex_to_decimal,
			rgb_hex)
	def test_rgb_hex_to_decimal_H(self):
		rgb_hex = 190
		self.assertRaises(TypeError,
			Themes().rgb_hex_to_decimal,
			rgb_hex)



class TestDecimalToRgbHex(unittest.TestCase):
	def test_decimal_to_rgb_hex_A(self):
		rgb_hex = "#ff00aa"
		rgb_dec = (255,0,170)
		self.assertEqual(
			Themes().decimal_to_rgb_hex(
				rgb_dec), rgb_hex)
	def test_decimal_to_rgb_hex_B(self):
		rgb_hex = "#0ac123"
		rgb_dec = (10,193,35)
		self.assertEqual(
			Themes().decimal_to_rgb_hex(
				rgb_dec), rgb_hex)
	def test_decimal_to_rgb_hex_C(self):
		rgb_hex = "#ffffff"
		rgb_dec = (255,255,255)
		self.assertEqual(
			Themes().decimal_to_rgb_hex(
				rgb_dec), rgb_hex)
	def test_decimal_to_rgb_hex_D(self):
		rgb_hex = "#aa44ab"
		rgb_dec = (170,68,171)
		self.assertEqual(
			Themes().decimal_to_rgb_hex(
				rgb_dec), rgb_hex)
	def test_decimal_to_rgb_hex_E(self):
		rgb_hex = "#aa44abc"
		self.assertRaises(TypeError,
			Themes().decimal_to_rgb_hex,
			rgb_hex)
	def test_decimal_to_rgb_hex_F(self):
		rgb_hex = "aa44ff"
		self.assertRaises(TypeError,
			Themes().decimal_to_rgb_hex,
			rgb_hex)
	def test_decimal_to_rgb_hex_G(self):
		rgb_hex = "blue"
		self.assertRaises(TypeError,
			Themes().decimal_to_rgb_hex,
			rgb_hex)
	def test_decimal_to_rgb_hex_H(self):
		rgb_hex = 190
		self.assertRaises(TypeError,
			Themes().decimal_to_rgb_hex,
			rgb_hex)



@unittest.skip('Deprecated, replaced with bicolor counterpart')
class TestGenerateAlphaRgbColor(unittest.TestCase):
	pass





class TestGenerateAlphaRgbBiColor(unittest.TestCase):

	def test_generate_alpha_rgb_bicolor_A(self):
		rgb1 = (0,0,128)
		rgb2 = (0,255,255)
		alpha = 0.5
		rgb_out = (0,128,192)
		self.assertEqual(
			Themes().generate_alpha_rgb_bicolor(rgb1,rgb2,alpha),
			rgb_out)


	def test_generate_alpha_rgb_bicolor_B(self):
		rgb1 = (170,0,0)
		rgb2 = (255,102,0)
		alpha = 0.3
		rgb_out = (230,72,0)
		self.assertEqual(
			Themes().generate_alpha_rgb_bicolor(rgb1,rgb2,alpha),
			rgb_out)


	def test_generate_alpha_rgb_bicolor_C(self):
		rgb1 = (0,128,0)
		rgb2 = (0,255,102)
		alpha = 0.08
		rgb_out = (0,245,94)
		self.assertEqual(
			Themes().generate_alpha_rgb_bicolor(rgb1,rgb2,alpha),
			rgb_out)



	def test_generate_alpha_rgb_bicolor_D(self):
		rgb1 = (170,0,136)
		rgb2 = (229,128,255)
		alpha = 0.785
		rgb_out = (183,28,162)
		self.assertEqual(
			Themes().generate_alpha_rgb_bicolor(rgb1,rgb2,alpha),
			rgb_out)


	def test_generate_alpha_rgb_bicolor_E(self):
		rgb1 = (255,0,0)
		rgb2 = (255,204,0)
		alpha = 0.199
		rgb_out = (255,164,0)
		self.assertEqual(
			Themes().generate_alpha_rgb_bicolor(rgb1,rgb2,alpha),
			rgb_out)




	def test_generate_alpha_rgb_bicolor_F(self):
		rgb1 = (170,0,136)
		rgb2 = (229,128,255)
		alpha = 1.0
		rgb_out = (170,0,136)
		self.assertEqual(
			Themes().generate_alpha_rgb_bicolor(rgb1,rgb2,alpha),
			rgb_out)


	def test_generate_alpha_rgb_bicolor_G(self):
		rgb1 = (0,128,0)
		rgb2 = (0,255,102)
		alpha = 0.98
		rgb_out = (0,131,3)
		self.assertEqual(
			Themes().generate_alpha_rgb_bicolor(rgb1,rgb2,alpha),
			rgb_out)


	def test_generate_alpha_rgb_bicolor_H(self):
		rgb1 = (0,128,0)
		rgb2 = (0,255,102)
		alpha = 0.0
		rgb_out = (0,255,102)
		self.assertEqual(
			Themes().generate_alpha_rgb_bicolor(rgb1,rgb2,alpha),
			rgb_out)


	def test_generate_alpha_rgb_bicolor_I(self):
		rgb1 = (255,0,0)
		rgb2 = (255,204,0)
		alpha = 0.0
		rgb_out = (255,204,0)
		self.assertEqual(
			Themes().generate_alpha_rgb_bicolor(rgb1,rgb2,alpha),
			rgb_out)





class TestIsColorName(unittest.TestCase):
	def test_is_color_name_A(self):
		color_name = "green"
		self.assertTrue(
			Themes().is_color_name(color_name))


	def test_is_color_name_B(self):
		color_name = "blue"
		self.assertTrue(
			Themes().is_color_name(color_name))


	def test_is_color_name_C(self):
		color_name = "black"
		self.assertTrue(
			Themes().is_color_name(color_name))


	def test_is_color_name_D(self):
		color_name = "purple"
		self.assertTrue(
			Themes().is_color_name(color_name))


	def test_is_color_name_E(self):
		color_name = "lightgray"
		self.assertFalse(
			Themes().is_color_name(color_name))


	def test_is_color_name_F(self):
		color_name = 897429
		self.assertFalse(
			Themes().is_color_name(color_name))


	def test_is_color_name_G(self):
		color_name = "pink"
		self.assertFalse(
			Themes().is_color_name(color_name))