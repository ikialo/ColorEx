import unittest
from colorexlib.colorexlib.common.datastructures import TileGroup, TileGroups


class TestInit(unittest.TestCase):
	def setUp(self):
		self.tg1 = TileGroup(1, 9,label='label1')
		self.tg2 = TileGroup(10, 80,label='label2')
		self.tg3 = TileGroup(-15, 40,label='label3')
		self.tg4 = TileGroup(50, 89.3,label='label4')
		self.tg5 = TileGroup(None, 105,label='label5')
		self.tg6 = TileGroup(200, None,label='label6')
	def test___init__A(self):
		self.assertRaises(TypeError, TileGroups,
			self.tg1, self.tg2, list(), self.tg3)
	def test___init__B(self):
		self.assertRaises(TypeError, TileGroups,
			self.tg6, False, False)
	def test___init__C(self):
		self.assertRaises(TypeError, TileGroups,
			17, self.tg4, self.tg2, self.tg6)
	def test___init__D(self):
		self.assertRaises(TypeError, TileGroups,
			self.tg1, self.tg2, self.tg3, dict())



@unittest.skip('Cannot access and test a private class method')
class TestValidate(unittest.TestCase):
	pass


@unittest.skip('Cannot access and test a private class method')
class TestIsNumeric(unittest.TestCase):
	pass

@unittest.skip('Cannot access and test a private class method')
class TestIsNone(unittest.TestCase):
	pass



class TestAlpha(unittest.TestCase):
	def setUp(self):
		self.tg1 = TileGroup(None, 10,label='label1')
		self.tg2 = TileGroup(10, 50,label='label2')
		self.tg3 = TileGroup(50, 100,label='label3')
		self.tg4 = TileGroup(100,None,label='label4')
		self.tilegroups1 = TileGroups(self.tg1, self.tg2,
			self.tg3, self.tg4)
	def test_alpha_A(self):
		self.assertRaises(TypeError, 
			self.tilegroups1.alpha, "eleven")
	def test_alpha_B(self):
		self.assertRaises(TypeError,
			self.tilegroups1.alpha, [1,2,3])
	def test_alpha_C(self):
		self.assertRaises(TypeError,
			self.tilegroups1.alpha, dict())
	def test_alpha_D(self):
		self.assertEqual(self.tilegroups1.alpha(60),
			0.75)
	def test_alpha_E(self):
		self.assertEqual(self.tilegroups1.alpha(15),
			0.50)
	def test_alpha_F(self):
		self.assertEqual(self.tilegroups1.alpha(5.66),
			0.25)






class TestGroup(unittest.TestCase):
	def setUp(self):
		self.tg1 = TileGroup(None, 10,label='label1')
		self.tg2 = TileGroup(10, 50,label='label2')
		self.tg3 = TileGroup(50, 100,label='label3')
		self.tg4 = TileGroup(100, 1000,label='label4')
		self.tg5 = TileGroup(1000, 1200,label='label5')
		self.tilegroups1 = TileGroups(
			self.tg1, self.tg2,self.tg3,
			self.tg4, self.tg5)
	def test_group_A(self):
		self.assertEqual(
			self.tilegroups1.group(-45),
			self.tg1)
	def test_group_B(self):
		self.assertEqual(
			self.tilegroups1.group(89),
			self.tg3)
	def test_group_C(self):
		self.assertEqual(
			self.tilegroups1.group(897),
			self.tg4)
	def test_group_D(self):
		self.assertEqual(
			self.tilegroups1.group(99.998),
			self.tg3)
	def test_group_E(self):
		self.assertIsNone(
			self.tilegroups1.group(1299),
			self.tg5)
	def test_group_F(self):
		self.assertRaises(TypeError,
			self.tilegroups1.group,'sixty')





class TestLabel(unittest.TestCase):
	def setUp(self):
		self.tg1 = TileGroup(None, 10,label='label1')
		self.tg2 = TileGroup(10, 50,label='label2')
		self.tg3 = TileGroup(50, 100,label='label3')
		self.tg4 = TileGroup(100, 1000,label='label4')
		self.tg5 = TileGroup(1000, 1200,label='label5')
		self.tilegroups1 = TileGroups(
			self.tg1, self.tg2,self.tg3,
			self.tg4, self.tg5)
	def test_label_A(self):
		self.assertEqual(
			self.tilegroups1.label(-45),
			'label1')
	def test_label_B(self):
		self.assertEqual(
			self.tilegroups1.label(89),
			'label3')
	def test_label_C(self):
		self.assertEqual(
			self.tilegroups1.label(897),
			'label4')
	def test_label_D(self):
		self.assertEqual(
			self.tilegroups1.label(99.998),
			'label3')
	def test_label_E(self):
		self.assertIsNone(
			self.tilegroups1.label(1299),
			'label5')
	def test_label_F(self):
		self.assertRaises(TypeError,
			self.tilegroups1.label,'sixty')
	def test_label_G(self):
		self.assertFalse(self.tilegroups1.label(15)
			== 'label5')






class TestStr(unittest.TestCase):
	def setUp(self):
		self.tg1 = TileGroup(None, 10,label='label1')
		self.tg2 = TileGroup(10, 50,label='label2')
		self.tg3 = TileGroup(50, 100,label='label3')
		self.tg4 = TileGroup(100, 1000,label='label4')
		self.tg5 = TileGroup(1000, 1200,label='label5')
		self.tilegroups1 = TileGroups(
			self.tg1, self.tg2,self.tg3,
			self.tg4, self.tg5)
		self.tilegroups2 = TileGroups(
			self.tg2, self.tg1, self.tg3,
			self.tg5, self.tg4)
	def test___str__A(self):
		str_rep = "TileGroups(" + \
			str(self.tg1) + ", " + str(self.tg2) + ", " + \
			str(self.tg3) + ", " + str(self.tg4) + ", " + \
			str(self.tg5) + ")"
		self.assertEqual(self.tilegroups1.__str__(),
			str_rep)

	def test___str__B(self):
		str_rep = "TileGroups(" + \
			str(self.tg2) + ", " + str(self.tg1) + ", " + \
			str(self.tg3) + ", " + str(self.tg5) + ", " + \
			str(self.tg4) + ")"
		self.assertEqual(self.tilegroups2.__str__(),
			str_rep)




class TestRepr(unittest.TestCase):
	def setUp(self):
		self.tg1 = TileGroup(None, 10,label='label1')
		self.tg2 = TileGroup(10, 50,label='label2')
		self.tg3 = TileGroup(50, 100,label='label3')
		self.tg4 = TileGroup(100, 1000,label='label4')
		self.tg5 = TileGroup(1000, 1200,label='label5')
		self.tilegroups1 = TileGroups(
			self.tg1, self.tg2,self.tg3,
			self.tg4, self.tg5)
		self.tilegroups2 = TileGroups(
			self.tg2, self.tg1, self.tg3,
			self.tg5, self.tg4)
	def test___repr__A(self):
		str_rep = "TileGroups(" + \
			repr(self.tg1) + ", " + repr(self.tg2) + ", " + \
			repr(self.tg3) + ", " + repr(self.tg4) + ", " + \
			repr(self.tg5) + ")"
		self.assertEqual(self.tilegroups1.__repr__(),
			str_rep)

	def test___repr__B(self):
		str_rep = "TileGroups(" + \
			repr(self.tg2) + ", " + repr(self.tg1) + ", " + \
			repr(self.tg3) + ", " + repr(self.tg5) + ", " + \
			repr(self.tg4) + ")"
		self.assertEqual(self.tilegroups2.__repr__(),
			str_rep)