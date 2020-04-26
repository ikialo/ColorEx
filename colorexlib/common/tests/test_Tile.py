import unittest
from ..datastructures import Tile




class TestInit(unittest.TestCase):
    def test__init__A(self):
    	self.assertRaises(TypeError, Tile)
    def test__init__B(self):
    	self.assertRaises(TypeError, Tile, {'label': 'test', 'valuel': 29, 
    		'rgb': '#ff00aa', 'alpha': 0.1})
    def test__init__C(self):
    	self.assertRaises(TypeError, Tile, {'value': 29, 
    		'rgb': '#ff00aa', 'alphaz': 0.1})
    def test__init__D(self):
    	self.assertRaises(TypeError, Tile, {'value': 29, 
    		'rgbz': '#ff00aa', 'alpha': 0.1})
    def test__init__E(self):
    	self.assertRaises(ValueError, Tile, {'value': 100, 
    		'rgb': '#ff00aa', 'alpha': 10})
    def test__init__F(self):
    	self.assertRaises(ValueError, Tile, {'value': 100, 
    		'rgb': '#ff00aaa', 'alpha': 0.1})
    def test__init__G(self):
    	self.assertRaises(ValueError, Tile, {'value': 100, 
    		'rgb': '#ff00aall', 'alpha': 0.1})
    def test__init__H(self):
    	self.assertRaises(ValueError, Tile, {'value': 100, 
    		'rgb': 'ff00aa', 'alpha': 0.1})
    def test__init__I(self):
    	self.assertRaises(TypeError, Tile, {'value': 'louis', 
    		'rgb': '#ff00aa', 'alpha': 0.1})
    def test__init__J(self):
    	self.assertRaises(TypeError, Tile, {'value': 12, 
    		'rgb': '#ff00aa', 'alpha': 'louis'})
    def test__init__L(self):
    	self.assertRaises(TypeError, Tile, {'value': 12, 
    		'rgb': '#ff00aa', 'alpha': None})




class TestValue(unittest.TestCase):
	def setUp(self):
		self.options1 = {'label': 'L1', 'rgb': '#ff00aa', 'value': 59, 'alpha': 0.88}
		self.options2 = {'label': 'L2', 'rgb': '#ff00aa', 'value': -56, 'alpha': 0.43}
		self.options3 = {'label': 'L3', 'rgb': '#ff00aa', 'value': 0x234, 'alpha': 0.43}
		self.options4 = {'label': 'L4', 'rgb': '#ff00aa', 'value': 102, 'alpha': 0.43}
		self.tile1 = Tile(self.options1)
		self.tile2 = Tile(self.options2)
		self.tile3 = Tile(self.options3)
		self.tile4 = Tile(self.options4)
	def test_value_A(self):
		self.assertEqual(self.tile1.value, self.options1['value'])
	def test_value_B(self):
		self.assertEqual(self.tile2.value, self.options2['value'])
	def test_value_C(self):
		self.assertEqual(self.tile3.value, self.options3['value'])
	def test_value_D(self):
		self.assertEqual(self.tile4.value, self.options4['value'])







class TestAlpha(unittest.TestCase):
	def setUp(self):
		self.options1 = {'label': 'L1', 'rgb': '#ff00aa', 'value': 59, 'alpha': 0.88}
		self.options2 = {'label': 'L2', 'rgb': '#ff00aa', 'value': -56, 'alpha': 0.43}
		self.options3 = {'label': 'L3', 'rgb': '#ff00aa', 'value': 0x234, 'alpha': 0.43}
		self.options4 = {'label': 'L4', 'rgb': '#ff00aa', 'value': 102, 'alpha': 0.43}
		self.tile1 = Tile(self.options1)
		self.tile2 = Tile(self.options2)
		self.tile3 = Tile(self.options3)
		self.tile4 = Tile(self.options4)
	def test_alpha_A(self):
		self.assertEqual(self.tile1.alpha, self.options1['alpha'])
	def test_alpha_B(self):
		self.assertEqual(self.tile2.alpha, self.options2['alpha'])
	def test_alpha_C(self):
		self.assertEqual(self.tile3.alpha, self.options3['alpha'])
	def test_alpha_D(self):
		self.assertEqual(self.tile4.alpha, self.options4['alpha'])











class TestRgb(unittest.TestCase):
	def setUp(self):
		self.options1 = {'label': 'L1', 'rgb': '#ff00aa', 'value': 59, 'alpha': 0.88}
		self.options2 = {'label': 'L2', 'rgb': '#ffaaaa', 'value': -56, 'alpha': 0.43}
		self.options3 = {'label': 'L3', 'rgb': '#ff1baa', 'value': 0x234, 'alpha': 0.43}
		self.options4 = {'label': 'L4', 'rgb': '#23f0aa', 'value': 102, 'alpha': 0.43}
		self.tile1 = Tile(self.options1)
		self.tile2 = Tile(self.options2)
		self.tile3 = Tile(self.options3)
		self.tile4 = Tile(self.options4)
	def test_rgb_A(self):
		self.assertEqual(self.tile1.rgb, self.options1['rgb'])
	def test_rgb_B(self):
		self.assertEqual(self.tile2.rgb, self.options2['rgb'])
	def test_rgb_C(self):
		self.assertEqual(self.tile3.rgb, self.options3['rgb'])
	def test_rgb_D(self):
		self.assertEqual(self.tile4.rgb, self.options4['rgb'])











class TestOptions(unittest.TestCase):
	def setUp(self):
		self.options1 = {'label': 'L1', 'rgb': '#ff00aa', 'value': 59, 'alpha': 0.88}
		self.options2 = {'label': 'L2', 'rgb': '#ffaaaa', 'value': -56, 'alpha': 0.43}
		self.options3 = {'label': 'L3', 'rgb': '#ff1baa', 'value': 0x234, 'alpha': 0.43}
		self.options4 = {'label': 'L4', 'rgb': '#23f0aa', 'value': 102, 'alpha': 0.43}
		self.tile1 = Tile(self.options1)
		self.tile2 = Tile(self.options2)
		self.tile3 = Tile(self.options3)
		self.tile4 = Tile(self.options4)
	def test_options_A(self):
		self.assertEqual(self.tile1.options, self.options1)
	def test_options_B(self):
		self.assertEqual(self.tile2.options, self.options2)
	def test_options_C(self):
		self.assertEqual(self.tile3.options, self.options3)
	def test_options_D(self):
		self.assertEqual(self.tile4.options, self.options4)








class TestLabel(unittest.TestCase):
	def setUp(self):
		self.options1 = {'label': 'L1', 'rgb': '#ff00aa', 'value': 59, 'alpha': 0.88}
		self.options2 = {'label': 'L2', 'rgb': '#ffaaaa', 'value': -56, 'alpha': 0.43}
		self.options3 = {'label': 'L3', 'rgb': '#ff1baa', 'value': 0x234, 'alpha': 0.43}
		self.options4 = {'label': 'L4', 'rgb': '#23f0aa', 'value': 102, 'alpha': 0.43}
		self.options5 = {'rgb': '#4455aa', 'value': -56, 'alpha': 0.991}
		self.options6 = {'rgb': '#aaff11', 'value': 1908, 'alpha': 0.2345}
		self.tile1 = Tile(self.options1)
		self.tile2 = Tile(self.options2)
		self.tile3 = Tile(self.options3)
		self.tile4 = Tile(self.options4)
		self.tile5 = Tile(self.options5)
		self.tile6 = Tile(self.options6)
	def test_label_A(self):
		self.assertEqual(self.tile1.label, self.options1['label'])
	def test_label_B(self):
		self.assertEqual(self.tile2.label, self.options2['label'])
	def test_label_C(self):
		self.assertEqual(self.tile3.label, self.options3['label'])
	def test_label_D(self):
		self.assertEqual(self.tile4.label, self.options4['label'])
	def test_label_E(self):
		self.assertIsNone(self.tile5.label)
	def test_label_F(self):
		self.assertIsNone(self.tile6.label)




class TestStr(unittest.TestCase):
	def setUp(self):
		self.options1 = {'label': 'L3', 'rgb': '#ff1baa', 'value': 0x234, 'alpha': 0.43}
		self.options2 = {'label': 'L4', 'rgb': '#23f0aa', 'value': 102, 'alpha': 0.43}
		self.options3 = {'rgb': '#4455aa', 'value': -56, 'alpha': 0.991}
		self.options4 = {'rgb': '#aaff11', 'value': 1908, 'alpha': 0.2345}
		self.tile1 = Tile(self.options1)
		self.tile2 = Tile(self.options2)
		self.tile3 = Tile(self.options3)
		self.tile4 = Tile(self.options4)
	def test___str__A(self):
		self.assertEqual(self.tile1.__str__(), "Tile("+str(self.options1)+")")
	def test___str__B(self):
		self.assertEqual(self.tile2.__str__(), "Tile("+str(self.options2)+")")
	def test___str__C(self):
		self.assertEqual(self.tile3.__str__(), "Tile("+str(self.options3)+")")
	def test___str__D(self):
		self.assertEqual(self.tile4.__str__(), "Tile("+str(self.options4)+")")







class TestRepr(unittest.TestCase):
	def setUp(self):
		self.options1 = {'label': 'L3', 'rgb': '#ff1baa', 'value': 0x234, 'alpha': 0.43}
		self.options2 = {'label': 'L4', 'rgb': '#23f0aa', 'value': 102, 'alpha': 0.43}
		self.options3 = {'rgb': '#4455aa', 'value': -56, 'alpha': 0.991}
		self.options4 = {'rgb': '#aaff11', 'value': 1908, 'alpha': 0.2345}
		self.tile1 = Tile(self.options1)
		self.tile2 = Tile(self.options2)
		self.tile3 = Tile(self.options3)
		self.tile4 = Tile(self.options4)
	def test___repr__A(self):
		self.assertEqual(self.tile1.__repr__(), "Tile("+repr(self.options1)+")")
	def test___repr__B(self):
		self.assertEqual(self.tile2.__repr__(), "Tile("+repr(self.options2)+")")
	def test___repr__C(self):
		self.assertEqual(self.tile3.__repr__(), "Tile("+repr(self.options3)+")")
	def test___repr__D(self):
		self.assertEqual(self.tile4.__repr__(), "Tile("+repr(self.options4)+")")







class TestLessThan(unittest.TestCase):
	def setUp(self):
		self.options1 = {'label': 'L3', 'rgb': '#ff1baa', 'value': 0x234, 'alpha': 0.43}
		self.options2 = {'label': 'L4', 'rgb': '#23f0aa', 'value': 102, 'alpha': 0.43}
		self.options3 = {'rgb': '#4455aa', 'value': -56, 'alpha': 0.991}
		self.options4 = {'rgb': '#aaff11', 'value': 1908, 'alpha': 0.2345}
		self.tile1 = Tile(self.options1)
		self.tile2 = Tile(self.options2)
		self.tile3 = Tile(self.options3)
		self.tile4 = Tile(self.options4)
	def test___lt__A(self):
		self.assertTrue(self.tile2.__lt__(self.tile1))
	def test___lt__B(self):
		self.assertTrue(self.tile3.__lt__(self.tile4))
	def test___lt__C(self):
		self.assertFalse(self.tile4.__lt__(self.tile2))
	def test___lt__D(self):
		self.assertFalse(self.tile1.__lt__(self.tile3))






class TestGreaterThan(unittest.TestCase):
	def setUp(self):
		self.options1 = {'label': 'L3', 'rgb': '#ff1baa', 'value': 0x234, 'alpha': 0.43}
		self.options2 = {'label': 'L4', 'rgb': '#23f0aa', 'value': 102, 'alpha': 0.43}
		self.options3 = {'rgb': '#4455aa', 'value': -56, 'alpha': 0.991}
		self.options4 = {'rgb': '#aaff11', 'value': 1908, 'alpha': 0.2345}
		self.tile1 = Tile(self.options1)
		self.tile2 = Tile(self.options2)
		self.tile3 = Tile(self.options3)
		self.tile4 = Tile(self.options4)
	def test___gt__A(self):
		self.assertTrue(self.tile4.__gt__(self.tile2))
	def test___gt__B(self):
		self.assertTrue(self.tile1.__gt__(self.tile3))
	def test___gt__C(self):
		self.assertFalse(self.tile2.__gt__(self.tile1))
	def test___gt__D(self):
		self.assertFalse(self.tile3.__gt__(self.tile4))




class TestLessEqual(unittest.TestCase):
	def setUp(self):
		self.options1 = {'label': 'L3', 'rgb': '#ff1baa', 'value': 0x234, 'alpha': 0.43}
		self.options2 = {'label': 'L4', 'rgb': '#23f0aa', 'value': 102, 'alpha': 0.43}
		self.options3 = {'rgb': '#4455aa', 'value': -56, 'alpha': 0.991}
		self.options4 = {'rgb': '#aaff11', 'value': 1908, 'alpha': 0.2345}
		self.options5 = {'rgb': '#2aff11', 'value': -56, 'alpha': 0.2345}
		self.options6 = {'rgb': '#a7ff11', 'value': 0x234, 'alpha': 0.2345}
		self.tile1 = Tile(self.options1)
		self.tile2 = Tile(self.options2)
		self.tile3 = Tile(self.options3)
		self.tile4 = Tile(self.options4)
		self.tile5 = Tile(self.options5)
		self.tile6 = Tile(self.options6)
	def test___le__A(self):
		self.assertTrue(self.tile2.__le__(self.tile1))
	def test___le__B(self):
		self.assertTrue(self.tile3.__le__(self.tile4))
	def test___le__C(self):
		self.assertFalse(self.tile4.__le__(self.tile2))
	def test___le__D(self):
		self.assertFalse(self.tile1.__le__(self.tile3))
	def test___le__E(self):
		self.assertTrue(self.tile5.__le__(self.tile3))
	def test___le__F(self):
		self.assertTrue(self.tile6.__le__(self.tile1))








class TestGreaterEqual(unittest.TestCase):
	def setUp(self):
		self.options1 = {'label': 'L3', 'rgb': '#ff1baa', 'value': 0x234, 'alpha': 0.43}
		self.options2 = {'label': 'L4', 'rgb': '#23f0aa', 'value': 102, 'alpha': 0.43}
		self.options3 = {'rgb': '#4455aa', 'value': -56, 'alpha': 0.991}
		self.options4 = {'rgb': '#aaff11', 'value': 1908, 'alpha': 0.2345}
		self.options5 = {'rgb': '#2aff11', 'value': -56, 'alpha': 0.2345}
		self.options6 = {'rgb': '#a7ff11', 'value': 0x234, 'alpha': 0.2345}
		self.tile1 = Tile(self.options1)
		self.tile2 = Tile(self.options2)
		self.tile3 = Tile(self.options3)
		self.tile4 = Tile(self.options4)
		self.tile5 = Tile(self.options5)
		self.tile6 = Tile(self.options6)
	def test___ge__A(self):
		self.assertTrue(self.tile4.__ge__(self.tile2))
	def test___ge__B(self):
		self.assertTrue(self.tile1.__ge__(self.tile3))
	def test___ge__C(self):
		self.assertFalse(self.tile2.__ge__(self.tile1))
	def test___ge__D(self):
		self.assertFalse(self.tile3.__ge__(self.tile4))
	def test___ge__E(self):
		self.assertTrue(self.tile5.__ge__(self.tile3))
	def test___ge__F(self):
		self.assertTrue(self.tile6.__ge__(self.tile1))









class TestEqual(unittest.TestCase):
	def setUp(self):
		self.options1 = {'label': 'L3', 'rgb': '#ff1baa', 'value': 0x234, 'alpha': 0.43}
		self.options2 = {'label': 'L4', 'rgb': '#23f0aa', 'value': 102, 'alpha': 0.43}
		self.options3 = {'rgb': '#4455aa', 'value': -56, 'alpha': 0.991}
		self.options4 = {'rgb': '#aaff11', 'value': 1908, 'alpha': 0.2345}
		self.options5 = {'rgb': '#2aff11', 'value': -56, 'alpha': 0.2345}
		self.options6 = {'rgb': '#a7ff11', 'value': 0x234, 'alpha': 0.2345}
		self.tile1 = Tile(self.options1)
		self.tile2 = Tile(self.options2)
		self.tile3 = Tile(self.options3)
		self.tile4 = Tile(self.options4)
		self.tile5 = Tile(self.options5)
		self.tile6 = Tile(self.options6)
	def test___eq__A(self):
		self.assertFalse(self.tile4.__eq__(self.tile2))
	def test___eq__B(self):
		self.assertFalse(self.tile1.__eq__(self.tile3))
	def test___eq__C(self):
		self.assertFalse(self.tile2.__eq__(self.tile1))
	def test___eq__D(self):
		self.assertFalse(self.tile3.__eq__(self.tile4))
	def test___eq__E(self):
		self.assertTrue(self.tile5.__eq__(self.tile3))
	def test___eq__F(self):
		self.assertTrue(self.tile6.__eq__(self.tile1))








