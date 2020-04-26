import unittest
from ..datastructures import Data

class TestInit(unittest.TestCase):
    def test__init__A(self):
            self.assertRaises(TypeError, Data)
    def test__init__B(self):
            self.assertRaises(TypeError, Data, "test")
    def test__init__D(self):
    	self.assertIsInstance(Data(45), Data)
    def test__init__E(self):
    	self.assertIsInstance(Data(-90), Data)
    def test__init__F(self):
    	self.assertIsInstance(Data(0x90ff92), Data)
    def test__init__G(self):
    	self.assertIsInstance(Data(-0x90ff92), Data)




class TestValue(unittest.TestCase):
	def setUp(self):
		self.data1 = Data(10)
		self.data2 = Data(-92)
		self.data3 = Data(90.893)
		self.data4 = Data(0x234)
	def test_value_A(self):
		self.assertEqual(self.data1.value, 10)
	def test_value_A(self):
		self.assertEqual(self.data2.value, -92)
	def test_value_B(self):
		self.assertEqual(self.data3.value, 90.893)
	def test_value_C(self):
		self.assertEqual(self.data4.value, 0x234)





class TestStr(unittest.TestCase):
	def setUp(self):
		self.data1 = Data(10)
		self.data2 = Data(-92)
		self.data3 = Data(90.893)
		self.data4 = Data(0x234)
	def test__str__A(self):
		self.assertEqual(self.data1.__str__(), 'Data(10)')
	def test__str__B(self):
		self.assertEqual(self.data2.__str__(), 'Data(-92)')
	def test__str__C(self):
		self.assertEqual(self.data3.__str__(), 'Data(90.893)')
	def test__str__D(self):
		self.assertEqual(self.data4.__str__(), 'Data(564)')





class TestRepr(unittest.TestCase):
	def setUp(self):
		self.data1 = Data(10)
		self.data2 = Data(-92)
		self.data3 = Data(90.893)
		self.data4 = Data(0x234)
	def test__str__A(self):
		self.assertEqual(self.data1.__repr__(), 'Data(10)')
	def test__str__B(self):
		self.assertEqual(self.data2.__repr__(), 'Data(-92)')
	def test__str__C(self):
		self.assertEqual(self.data3.__repr__(), 'Data(90.893)')
	def test__str__D(self):
		self.assertEqual(self.data4.__repr__(), 'Data(564)')




class TestLessThan(unittest.TestCase):
	def setUp(self):
		self.data1 = Data(10)
		self.data2 = Data(-92)
		self.data3 = Data(90.893)
		self.data4 = Data(0x234)
	def test__lt__A(self):
		self.assertTrue(self.data2.__lt__(self.data1))
	def test__lt__B(self):
		self.assertTrue(self.data1.__lt__(self.data3))
	def test__lt__C(self):
		self.assertTrue(self.data1.__lt__(self.data4))
	def test__lt__D(self):
		self.assertFalse(self.data1.__lt__(self.data2))
	def test__lt__E(self):
		self.assertFalse(self.data3.__lt__(self.data1))
	def test__lt__F(self):
		self.assertFalse(self.data4.__lt__(self.data1))
	def test__lt__G(self):
		self.assertTrue(self.data2 <= self.data1)
	def test__lt__H(self):
		self.assertTrue(self.data3 <= self.data4)
	def test__lt__I(self):
		self.assertFalse(self.data4 <= self.data1)
	def test__lt__J(self):
		self.assertFalse(self.data3 <= self.data1)



class TestGreaterThan(unittest.TestCase):
	def setUp(self):
		self.data1 = Data(10)
		self.data2 = Data(-92)
		self.data3 = Data(90.893)
		self.data4 = Data(0x234)
	def test__gt__A(self):
		self.assertTrue(self.data1.__gt__(self.data2))
	def test__gt__B(self):
		self.assertTrue(self.data3.__gt__(self.data2))
	def test__gt__C(self):
		self.assertTrue(self.data3.__gt__(self.data1))
	def test__gt__D(self):
		self.assertTrue(self.data4.__gt__(self.data3))
	def test__gt__E(self):
		self.assertFalse(self.data1.__gt__(self.data4))
	def test__gt__F(self):
		self.assertFalse(self.data2.__gt__(self.data3))
	def test__gt__G(self):
		self.assertTrue(self.data1 > self.data2)
	def test__gt__H(self):
		self.assertTrue(self.data3 > self.data2)
	def test__gt__I(self):
		self.assertTrue(self.data4 > self.data1)
	def test__gt__J(self):
		self.assertFalse(self.data2 > self.data4)
	def test__gt__K(self):
		self.assertFalse(self.data3 > self.data4)




class TestLessEqual(unittest.TestCase):
	def setUp(self):
		self.data1 = Data(10)
		self.data2 = Data(-92)
		self.data3 = Data(90.893)
		self.data4 = Data(0x234)
		self.data5 = Data(90.893)
	def test__le__A(self):
		self.assertTrue(self.data1.__le__(self.data3))
	def test__le__B(self):
		self.assertTrue(self.data2.__le__(self.data1))
	def test__le__C(self):
		self.assertTrue(self.data5.__le__(self.data4))
	def test__le__D(self):
		self.assertTrue(self.data5.__le__(self.data3))
	def test__le__E(self):
		self.assertFalse(self.data1.__le__(self.data2))
	def test__le__F(self):
		self.assertFalse(self.data4.__le__(self.data5))
	def test__le__G(self):
		self.assertTrue(self.data1 <= self.data3)
	def test__le__H(self):
		self.assertTrue(self.data2 <= self.data1)
	def test__le__I(self):
		self.assertTrue(self.data5 <= self.data4)
	def test__le__J(self):
		self.assertTrue(self.data5 <= self.data3)
	def test__le__K(self):
		self.assertFalse(self.data1 <= self.data2)
	def test__le__L(self):
		self.assertFalse(self.data4 <= self.data5)







class TestGreaterEqual(unittest.TestCase):
	def setUp(self):
		self.data1 = Data(10)
		self.data2 = Data(-92)
		self.data3 = Data(90.893)
		self.data4 = Data(0x234)
		self.data5 = Data(90.893)
	def test__ge__A(self):
		self.assertTrue(self.data1.__ge__(self.data2))
	def test__ge__B(self):
		self.assertTrue(self.data3.__ge__(self.data1))
	def test__ge__C(self):
		self.assertTrue(self.data4.__ge__(self.data5))
	def test__ge__D(self):
		self.assertTrue(self.data3.__ge__(self.data5))
	def test__ge__E(self):
		self.assertFalse(self.data2.__ge__(self.data1))
	def test__ge__F(self):
		self.assertFalse(self.data1.__ge__(self.data3))
	def test__ge__G(self):
		self.assertFalse(self.data5.__ge__(self.data4))
	def test__ge__H(self):
		self.assertTrue(self.data1 >=self.data2)
	def test__ge__I(self):
		self.assertTrue(self.data3 >=self.data1)
	def test__ge__J(self):
		self.assertTrue(self.data4 >=self.data5)
	def test__ge__K(self):
		self.assertTrue(self.data3 >=self.data5)
	def test__ge__L(self):
		self.assertFalse(self.data2 >=self.data1)
	def test__ge__M(self):
		self.assertFalse(self.data1 >=self.data3)
	def test__ge__N(self):
		self.assertFalse(self.data5 >=self.data4)



class TestEqual(unittest.TestCase):
	def setUp(self):
		self.data1 = Data(10)
		self.data2 = Data(-92)
		self.data3 = Data(90.893)
		self.data4 = Data(0x234)
		self.data5 = Data(90.893)
		self.data6 = Data(564)
		self.data7 = Data(10)
		self.data8 = Data(-92)
	def test__eq__A(self):
		self.assertTrue(self.data1.__eq__(self.data7))
	def test__eq__B(self):
		self.assertTrue(self.data2.__eq__(self.data8))
	def test__eq__C(self):
		self.assertTrue(self.data4.__eq__(self.data6))
	def test__eq__D(self):
		self.assertFalse(self.data1.__eq__(self.data8))
	def test__eq__E(self):
		self.assertFalse(self.data6.__eq__(self.data5))
	def test__eq__F(self):
		self.assertFalse(self.data3.__eq__(self.data7))
	def test__eq__G(self):
		self.assertTrue(self.data1 == self.data7)
	def test__eq__H(self):
		self.assertTrue(self.data2 == self.data8)
	def test__eq__I(self):
		self.assertTrue(self.data4 == self.data6)
	def test__eq__J(self):
		self.assertFalse(self.data1 == self.data8)
	def test__eq__K(self):
		self.assertFalse(self.data6 == self.data5)
	def test__eq__L(self):
		self.assertFalse(self.data3 == self.data7)






if __name__ == '__main__':
        unittest.main()
