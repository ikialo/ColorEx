import unittest
from colorexlib.colorexlib.common.datastructures import TileGroup


class TestInit(unittest.TestCase):
	def test___init__A(self):
		self.assertRaises(TypeError, TileGroup)
	def test___init__B(self):
		self.assertRaises(TypeError, TileGroup, 90)
	def test___init__C(self):
		self.assertRaises(TypeError, TileGroup, 90,'fourteen')
	def test___init__D(self):
		self.assertRaises(ValueError, TileGroup, 45,10)
	def test___init__E(self):
		self.assertRaises(ValueError, TileGroup, False, False)
	def test___init__F(self):
		self.assertRaises(TypeError, TileGroup, 'ten', False)
	def test___init__G(self):
		self.assertRaises(TypeError, TileGroup, None, None)





@unittest.skip('Cannot access and test a private class method')
class TestValidate(unittest.TestCase):
	pass






class TestStr(unittest.TestCase):
	def setUp(self):
		self.tg1 = TileGroup(1, 9,label='label1')
		self.tg2 = TileGroup(10, 80,label='label2')
		self.tg3 = TileGroup(-15, 40,label='label3')
		self.tg4 = TileGroup(50, 89.3,label='label4')
		self.tg5 = TileGroup(None, 105,label='label5')
		self.tg6 = TileGroup(200, None,label='label6')
	def test___str__A(self):
		self.assertEqual(self.tg1.__str__(),'label1 = (1,9)')
	def test___str__B(self):
		self.assertEqual(self.tg2.__str__(),'label2 = (10,80)')
	def test___str__C(self):
		self.assertEqual(self.tg3.__str__(),'label3 = (-15,40)')
	def test___str__D(self):
		self.assertEqual(self.tg4.__str__(),'label4 = (50,89.3)')
	def test___str__E(self):
		self.assertEqual(self.tg5.__str__(),'label5 = (-,105)')
	def test___str__F(self):
		self.assertEqual(self.tg6.__str__(),'label6 = (200,+)')




class TestRepr(unittest.TestCase):
	def setUp(self):
		self.tg1 = TileGroup(1, 9,label='label1')
		self.tg2 = TileGroup(10, 80,label='label2')
		self.tg3 = TileGroup(-15, 40,label='label3')
		self.tg4 = TileGroup(50, 89.3,label='label4')
		self.tg5 = TileGroup(None, 105,label='label5')
		self.tg6 = TileGroup(200, None,label='label6')
	def test___repr__A(self):
		self.assertEqual(self.tg1.__repr__(),'label1 = (1,9)')
	def test___repr__B(self):
		self.assertEqual(self.tg2.__repr__(),'label2 = (10,80)')
	def test___repr__C(self):
		self.assertEqual(self.tg3.__repr__(),'label3 = (-15,40)')
	def test___repr__D(self):
		self.assertEqual(self.tg4.__repr__(),'label4 = (50,89.3)')
	def test___repr__E(self):
		self.assertEqual(self.tg5.__repr__(),'label5 = (-,105)')
	def test___repr__F(self):
		self.assertEqual(self.tg6.__repr__(),'label6 = (200,+)')






class TestInGroup(unittest.TestCase):
	def setUp(self):
		self.tg1 = TileGroup(1, 9,label='label1')
		self.tg2 = TileGroup(10, 80,label='label2',inclusive_right=True)
		self.tg3 = TileGroup(-15, 40,label='label3')
		self.tg4 = TileGroup(50, 89.3,label='label4',inclusive_right=True)
		self.tg5 = TileGroup(None, 105,label='label5')
		self.tg6 = TileGroup(200, None,label='label6',inclusive_left=False)
	def test_in_group_A(self):
		self.assertRaises(TypeError,self.tg1.in_group,'twenty')
	def test_in_group_B(self):
		self.assertRaises(Exception,self.tg1.in_group,list())
	def test_in_group_C(self):
		self.assertTrue(self.tg1.in_group(5))
		self.assertFalse(self.tg1.in_group(-10))
		self.assertFalse(self.tg1.in_group(10))
		self.assertFalse(self.tg1.in_group(9))
	def test_in_group_D(self):
		self.assertTrue(self.tg2.in_group(20))
		self.assertTrue(self.tg2.in_group(45))
		self.assertTrue(self.tg2.in_group(80))
		self.assertFalse(self.tg2.in_group(81))
		self.assertFalse(self.tg2.in_group(9))
	def test_in_group_E(self):
		self.assertTrue(self.tg3.in_group(0))
		self.assertTrue(self.tg3.in_group(34))
		self.assertTrue(self.tg3.in_group(29.8922))
		self.assertFalse(self.tg3.in_group(-99))
		self.assertFalse(self.tg3.in_group(49))
		self.assertFalse(self.tg3.in_group(40))
	def test_in_group_F(self):
		self.assertTrue(self.tg4.in_group(78))
		self.assertTrue(self.tg4.in_group(70))
		self.assertTrue(self.tg4.in_group(50))
		self.assertTrue(self.tg4.in_group(89.3))
		self.assertFalse(self.tg4.in_group(89.4))
		self.assertFalse(self.tg4.in_group(49.99999))
	def test_in_group_G(self):
		self.assertTrue(self.tg5.in_group(-100.2))
		self.assertTrue(self.tg5.in_group(104))
		self.assertTrue(self.tg5.in_group(100))
		self.assertTrue(self.tg5.in_group(-89.33))
		self.assertFalse(self.tg5.in_group(105))
		self.assertFalse(self.tg5.in_group(67800))
		self.assertFalse(self.tg5.in_group(800))
	def test_in_group_H(self):
		self.assertTrue(self.tg6.in_group(560))
		self.assertTrue(self.tg6.in_group(1000))
		self.assertFalse(self.tg6.in_group(200))
		self.assertFalse(self.tg6.in_group(199))
		self.assertFalse(self.tg6.in_group(-10923.333))


