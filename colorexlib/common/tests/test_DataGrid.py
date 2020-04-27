import unittest
from ..datastructures import DataGrid


class TestInit(unittest.TestCase):
	def test___init__A(self):
		self.assertRaises(TypeError, DataGrid)
	def test___init__B(self):
		self.assertRaises(TypeError, DataGrid, 14)
	def test___init__C(self):
		self.assertRaises(TypeError, DataGrid, dict())
	def test___init__D(self):
		self.assertRaises(TypeError, DataGrid, [1,2,3])
	def test___init__E(self):
		self.assertRaises(TypeError, DataGrid, 'testing123')
	def test___init__F(self):
		self.data1 = [
			['',	'NCD', 	'ENB',	'WNB', 	'WWK', 'ORO'],
			['MON',	51,		13,		20,		19,		67],
			['TUE',	19,		890,	13,		2,		9],
			['WED',	15,		1,		1,		11,		100],
			['THUR',88,		24,		52,		95,		101]
		]
		self.datagrid1 = DataGrid({'data': self.data1})
		self.assertIsInstance(self.datagrid1, DataGrid)



class TestGrid(unittest.TestCase):
	def test_grid_A(self):
		self.data1 = [
			['',	'NCD', 	'ENB',	'WNB', 	'WWK', 'ORO'],
			['MON',	51,		13,		20,		19,		67],
			['TUE',	19,		890,	13,		2,		9],
			['WED',	15,		1,		1,		11,		100],
			['THUR',88,		24,		52,		95,		101]
		]
		self.datagrid1 = DataGrid({'data': self.data1})
		self.assertEqual(self.data1, self.datagrid1.grid)
	def test_grid_B(self):
		self.data1 = [
			['',	'NCD', 	'ENB',	'WNB', 	'WWK', 'ORO'],
			['MON',	51,		13,		20,		19,		67],
			['TUE',	19,		-890,	13,		2,		9],
			['WED',	15,		1,		1,		11,		100],
			['THUR',88,		24,		-52,	95,		101]
		]
		self.datagrid1 = DataGrid({'data': self.data1})
		self.assertEqual(self.data1, self.datagrid1.grid)
	def test_grid_C(self):
		self.data1 = [
			['',	'NCD', 	'ENB',	'WNB', 	'WWK', 'ORO'],
			['MON',	51.5,	13.09,	20,		19,		67],
			['TUE',	19,		890,	13,		2,		9],
			['WED',	15.14,	1,		1,		11,		100],
			['THUR',88,		24.4,	2.52,	95.0,	101]
		]
		self.datagrid1 = DataGrid({'data': self.data1})
		self.assertEqual(self.data1, self.datagrid1.grid)



class TestSize(unittest.TestCase):
	def test_size_A(self):
		self.data1 = [
			['',	'NCD', 	'ENB',	'WNB', 	'WWK', 'ORO'],
			['MON',	51.5,	13.09,	20,		19,		67],
			['TUE',	19,		890,	13,		2,		9],
			['WED',	15.14,	1,		1,		11,		100],
			['THUR',88,		24.4,	2.52,	95.0,	101]
		]
		self.datagrid1 = DataGrid({'data': self.data1})
		rows = len(self.data1)
		cols = len(self.data1[0])
		self.assertEqual(rows*cols, self.datagrid1.size)
	def test_size_B(self):
		self.data1 = [
			['',	'NCD', 	'ENB',	'WNB', 	'WWK', 'ORO'],
			['MON',	51,		13,		20,		19,		67],
			['TUE',	19,		890,	13,		2,		9],
			['WED',	15,		1,		1,		11,		100],
			['THUR',88,		24,		52,		95,		101]
		]
		self.datagrid1 = DataGrid({'data': self.data1})
		rows = len(self.data1)
		cols = len(self.data1[0])
		self.assertEqual(rows*cols, self.datagrid1.size)


class TestShape(unittest.TestCase):
	def test_shape_A(self):
		self.data1 = [
			['',	'NCD', 	'ENB',	'WNB', 	'WWK', 'ORO'],
			['MON',	51,		13,		20,		19,		67],
			['TUE',	19,		890,	13,		2,		9],
			['WED',	15,		1,		1,		11,		100],
			['THUR',88,		24,		52,		95,		101]
		]
		self.datagrid1 = DataGrid({'data': self.data1})
		rows = len(self.data1)
		cols = len(self.data1[0])
		self.assertEqual({'rows': rows, 'cols': cols}, self.datagrid1.shape)
	def test_shape_B(self):
		self.data1 = [
			['',	'NCD', 	'ENB',	'WNB', 	'WWK', 'ORO'],
			['MON',	51,		13,		20,		19,		67],
			['TUE',	19,		890,	13,		2,		9],
			['WED',	15,		1,		1,		11,		100],
			['THUR',88,		24,		52,		95,		101]
		]
		self.datagrid1 = DataGrid({'data': self.data1})
		rows = len(self.data1)
		cols = len(self.data1[0])
		self.assertEqual({'rows': rows, 'cols': cols}, self.datagrid1.shape)


class TestRows(unittest.TestCase):
	def test_rows_A(self):
		self.data1 = [
			['',	'NCD', 	'ENB',	'WNB', 	'WWK', 'ORO'],
			['MON',	51,		13,		20,		19,		67],
			['TUE',	19,		890,	13,		2,		9],
			['WED',	15,		1,		1,		11,		100],
			['THUR',88,		24,		52,		95,		101]
		]
		self.datagrid1 = DataGrid({'data': self.data1})
		rows = len(self.data1)
		self.assertEqual(rows, self.datagrid1.rows)
	def test_rows_B(self):
		self.data1 = [
			['',	'NCD', 	'ENB',	'WNB', 	'WWK', 'ORO'],
			['MON',	51,		13,		20,		19,		67],
			['TUE',	19,		890,	13,		2,		9],
			['WED',	15,		1,		1,		11,		100],
			['THUR',88,		24,		52,		95,		101]
		]
		self.datagrid1 = DataGrid({'data': self.data1})
		rows = len(self.data1)
		self.assertEqual(rows, self.datagrid1.rows)





class TestCols(unittest.TestCase):
	def test_cols_A(self):
		self.data1 = [
			['',	'NCD', 	'ENB',	'WNB', 	'WWK', 'ORO'],
			['MON',	51,		13,		20,		19,		67],
			['TUE',	19,		890,	13,		2,		9],
			['WED',	15,		1,		1,		11,		100],
			['THUR',88,		24,		52,		95,		101]
		]
		self.datagrid1 = DataGrid({'data': self.data1})
		cols = len(self.data1[0])
		self.assertEqual(cols, self.datagrid1.cols)
	def test_cols_B(self):
		self.data1 = [
			['',	'NCD', 	'ENB',	'WNB', 	'WWK', 'ORO'],
			['MON',	51,		13,		20,		19,		67],
			['TUE',	19,		890,	13,		2,		9],
			['WED',	15,		1,		1,		11,		100],
			['THUR',88,		24,		52,		95,		101]
		]
		self.datagrid1 = DataGrid({'data': self.data1})
		cols = len(self.data1[0])
		self.assertEqual(cols, self.datagrid1.cols)





class TestRowColHeaders(unittest.TestCase):
	def setUp(self):
		self.data1 = [
			['',	'NCD', 	'ENB',	'WNB', 	'WWK', 'ORO'],
			['MON',	51,		13,		20,		19,		67],
			['TUE',	19,		890,	13,		2,		9],
			['WED',	15,		1,		1,		11,		100],
			['THUR',88,		24,		52,		95,		101]
		]
		self.data2 = [
			['',	'NCD', 	'ENB',	'WNB', 	'WWK', 'ORO'],
			['MON',	51,		13,		20,		19,		67],
			['TUE',	19,		890,	13,		2,		9],
			['WED',	15,		1,		1,		11,		100],
			['THUR',88,		24,		52,		95,		101]
		]
		self.datagrid1 = DataGrid({'data': self.data1, 'rowcol_headers': True})
		self.datagrid2 = DataGrid({'data': self.data2, 'rowcol_headers': False})
	def test_rowcolheaders_A(self):
		self.assertTrue(self.datagrid1.rowcolheaders)
	def test_rowcolheaders_B(self):
		self.assertFalse(self.datagrid2.rowcolheaders)






class TestGetData(unittest.TestCase):
	def setUp(self):
		self.data1 = [
			['',	'NCD', 	'ENB',	'WNB', 	'WWK', 'ORO'],
			['MON',	51,		13,		20,		19,		67],
			['TUE',	19,		890,	13,		2,		9],
			['WED',	15,		1,		1,		11,		100],
			['THUR',88,		24,		52,		95,		101]
		]
		self.datagrid1 = DataGrid({'data': self.data1, 'rowcol_headers': True})
	def test_get_data_A(self):
		self.assertEqual(self.datagrid1.get_data(0,3), self.data1[0][3])
	def test_get_data_B(self):
		self.assertEqual(self.datagrid1.get_data(3,3), self.data1[3][3])
	def test_get_data_C(self):
		self.assertRaises(IndexError,self.datagrid1.get_data,100,3)
	def test_get_data_D(self):
		self.assertRaises(TypeError,self.datagrid1.get_data,'24',3)
	def test_get_data_E(self):
		self.assertRaises(TypeError,self.datagrid1.get_data,3,'104.4')
	def test_get_data_F(self):
		self.assertRaises(TypeError,self.datagrid1.get_data,3.2,3.98)





class TestGetMaxValue(unittest.TestCase):
	def setUp(self):
		self.max1 = 1004
		self.max2 = 987
		self.data1 = [
			['',	'NCD', 	'ENB',	'WNB', 	'WWK', 'ORO'],
			['MON',	51,		13,		20,		19,		67],
			['TUE',	19,		890,	13,		2,		9],
			['WED',	15,		self.max1, 1,	11,		100],
			['THUR',88,		24,		52,		95,		101]
		]
		self.data2 = [
			[103,	51,		13,		20,		19,		67],
			[self.max2,	19,	890,	13,		2,		9],
			[4,		15,		1,		1,		11,		100],
			[0,		88,		24,		52,		95,		101]
		]
		self.datagrid1 = DataGrid({'data': self.data1, 'rowcol_headers': True})
		self.datagrid2 = DataGrid({'data': self.data2, 'rowcol_headers': False})
	def test_get_max_value_A(self):
		self.assertEqual(self.datagrid1.get_max_value(),self.max1)
	def test_get_max_value_B(self):
		self.assertEqual(self.datagrid2.get_max_value(), self.max2)







class TestGetMinValue(unittest.TestCase):
	def setUp(self):
		self.min1 = -1
		self.min2 = 0
		self.data1 = [
			['',	'NCD', 	'ENB',	'WNB', 	'WWK', 'ORO'],
			['MON',	51,		13,		20,		19,		67],
			['TUE',	19,		890,	13,		2,		9],
			['WED',	15,		self.min1, 1,	11,		100],
			['THUR',88,		24,		52,		95,		101]
		]
		self.data2 = [
			[103,	51,		13,		20,		19,		67],
			[self.min2,	19,	890,	13,		2,		9],
			[4,		15,		1,		1,		11,		100],
			[0,		88,		24,		52,		95,		101]
		]
		self.datagrid1 = DataGrid({'data': self.data1, 'rowcol_headers': True})
		self.datagrid2 = DataGrid({'data': self.data2, 'rowcol_headers': False})
	def test_get_min_value_A(self):
		self.assertEqual(self.datagrid1.get_min_value(),self.min1)
	def test_get_min_value_B(self):
		self.assertEqual(self.datagrid2.get_min_value(), self.min2)




@unittest.skip("Cannot access and tests a private class method, hence.")
class TestCalculateSize(unittest.TestCase):
	pass







@unittest.skip("Cannot access and tests a private class method, hence.")
class TestCalculateShape(unittest.TestCase):
	pass







class TestStr(unittest.TestCase):
	def setUp(self):
		self.data1 = [
			['',	'NCD', 	'ENB',	'WNB', 	'WWK', 'ORO'],
			['MON',	51,		13,		20,		19,		67],
			['TUE',	19,		890,	13,		2,		9],
			['WED',	15,		1,		1,		11,		100],
			['THUR',88,		24,		52,		95,		101]
		]
		self.data2 = [
			['',	'NCD', 	'ENB',	'WNB', 	'WWK', 'ORO'],
			['MON',	51,		13,		20,		19,		67],
			['TUE',	15,		890,	1,		2,		19],
			['WED',	15,		1,		1,		11,		100],
			['THUR',88,		24,		5,		951,	101]
		]
		self.datagrid1 = DataGrid({'data': self.data1, 'rowcol_headers': True})
		self.datagrid2 = DataGrid({'data': self.data2, 'rowcol_headers': False})
	def test___str__A(self):
		dg1_str = 'DataGrid('+str(self.data1)+')'
		self.assertEqual(self.datagrid1.__str__(), dg1_str)
	def test___str__B(self):
		dg2_str = 'DataGrid('+str(self.data2)+')'
		self.assertEqual(self.datagrid2.__str__(), dg2_str)










class TestRepr(unittest.TestCase):
	def setUp(self):
		self.data1 = [
			['',	'NCD', 	'ENB',	'WNB', 	'WWK', 'ORO'],
			['MON',	51,		13,		20,		19,		67],
			['TUE',	19,		890,	13,		2,		9],
			['WED',	15,		1,		1,		11,		100],
			['THUR',88,		24,		52,		95,		101]
		]
		self.data2 = [
			['',	'NCD', 	'ENB',	'WNB', 	'WWK', 'ORO'],
			['MON',	51,		13,		20,		19,		67],
			['TUE',	15,		890,	1,		2,		19],
			['WED',	15,		1,		1,		11,		100],
			['THUR',88,		24,		5,		951,	101]
		]
		self.datagrid1 = DataGrid({'data': self.data1, 'rowcol_headers': True})
		self.datagrid2 = DataGrid({'data': self.data2, 'rowcol_headers': False})
	def test___repr__A(self):
		dg1_repr = 'DataGrid('+repr(self.data1)+')'
		self.assertEqual(self.datagrid1.__repr__(), dg1_repr)
	def test___repr__B(self):
		dg2_repr = 'DataGrid('+repr(self.data2)+')'
		self.assertEqual(self.datagrid2.__repr__(), dg2_repr)










class TestEqual(unittest.TestCase):
	def setUp(self):
		self.data1 = [
			['',	'NCD', 	'ENB',	'WNB', 	'WWK', 'ORO'],
			['MON',	51,		13,		20,		19,		67],
			['TUE',	19,		890,	13,		2,		9],
			['WED',	15,		1,		1,		11,		100],
			['THUR',88,		24,		52,		95,		101]
		]
		self.data2 = [
			['',	'NCD', 	'ENB',	'WNB',	'WWK', 'ORO'],
			['MON',	51,		13,		20,		19,		67],
			['TUE',	19,		890,	13,		2,		9],
			['WED',	15,		1,		1,		11,		100],
			['THUR',88,		24,		52,		95,		101]
		]
		self.data3 = [
			['',	'NCDA',	'ENB',	'WNB', 	'WWK', 'ORO'],
			['MON',	1,		13,		20,		19,		67],
			['TUE',	15,		890,	1,		2,		19],
			['WED',	15,		1,		1,		11,		100],
			['THUR',88,		24,		5,		951,	101]
		]
		self.datagrid1 = DataGrid({'data': self.data1, 'rowcol_headers': True})
		self.datagrid2 = DataGrid({'data': self.data2, 'rowcol_headers': False})
		self.datagrid3 = DataGrid({'data': self.data3, 'rowcol_headers': False})
	def test___eq__A(self):
		self.assertEqual(self.datagrid1,self.datagrid2)
		self.assertTrue(self.datagrid1 == self.datagrid2)
	def test___eq__B(self):
		self.assertNotEqual(self.datagrid1,self.datagrid3)
		self.assertTrue(self.datagrid1 != self.datagrid3)
	def test___eq__C(self):
		self.assertNotEqual(self.datagrid2,self.datagrid3)
		self.assertTrue(self.datagrid2 != self.datagrid3)



