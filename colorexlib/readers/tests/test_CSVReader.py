import unittest
from colorexlib.colorexlib.readers.CSVReader import CSVReader
from colorexlib.colorexlib.common.datastructures import Data, DataGrid


class TestInit(unittest.TestCase):
	def test___init__A(self):
		path = "colorexlib/colorexlib/readers/tests/test_website_traffic.csv"
		CSVReader(path, rowcol_headers=False)

	def test___init__B(self):
		path = "colorexlib/colorexlib/readers/tests/test_website_traffic2.csv"
		self.assertRaises(FileNotFoundError,
			CSVReader, path, rowcol_headers=False)

	def test___init__C(self):
		self.assertRaises(TypeError,
			CSVReader)
	



class TestRowColHeaders(unittest.TestCase):
	def setUp(self):
		self.path = "colorexlib/colorexlib/readers/tests/test_website_traffic.csv"
		self.reader1 = CSVReader(self.path, rowcol_headers=False)
		self.reader2 = CSVReader(self.path, rowcol_headers=True)
		self.reader3 = CSVReader(self.path)

	def test_rowcolheaders_A(self):
		self.assertEqual(self.reader1.rowcolheaders,
			False)
		self.assertEqual(self.reader2.rowcolheaders,
			True)
		self.assertEqual(self.reader3.rowcolheaders,
			True)



class TestRead(unittest.TestCase):
	def setUp(self):
		self.path = "colorexlib/colorexlib/readers/tests/test_website_traffic.csv"
		self.reader1 = CSVReader(self.path, rowcol_headers=False)
		self.reader2 = CSVReader(self.path, rowcol_headers=True)
		self.reader3 = CSVReader(self.path)
		self.data_withheaders = [
			["Month","Web Traffic","Call to actions"],
			["January",100,50],
			["February",1000,900],
			["March",14500,8000],
			["April",14500,900],
			["May",9000,12313],
			["June",15699,54],
			["July",200456,234],
			["August",34233,512],
			["September",231231,123],
			["October",128293,543],
			["November",234234,123],
			["December",111111,445585]
		]

	def test_read_A(self):
		self.assertEqual(self.reader1.data,
			self.data_withheaders)

	def test_read_B(self):
		self.assertEqual(self.reader2.data,
			self.data_withheaders)

	def test_read_C(self):
		self.assertEqual(self.reader3.data,
			self.data_withheaders)




class TestRowToFloat(unittest.TestCase):
	def setUp(self):
		self.path = "colorexlib/colorexlib/readers/tests/test_website_traffic.csv"
		self.reader = CSVReader(self.path, rowcol_headers=False)

	def test_row_to_float_A(self):
		rowcolheaders = True
		mock_input_1 = ["Label 1",80,90,100]
		mock_output_1 = ["Label 1", 80.00, 90.0, 100.0]
		self.assertEqual(self.reader.row_to_float(
			mock_input_1, rowcolheaders),mock_output_1)

	def test_row_to_float_B(self):
		rowcolheaders = True
		mock_input_1 = [1090,80,90,100]
		mock_output_1 = ["1090", 80.0, 90.0, 100.0]
		self.assertEqual(self.reader.row_to_float(
			mock_input_1, rowcolheaders),mock_output_1)


	def test_row_to_float_C(self):
		rowcolheaders = False
		mock_input_1 = ["Test",80,90,100]
		mock_output_1 = ["Test", 80.0, 90.0, 100.0]
		self.assertEqual(self.reader.row_to_float(
			mock_input_1, rowcolheaders),mock_output_1)

	def test_row_to_float_D(self):
		rowcolheaders = False
		mock_input_1 = ["90",80,90,100]
		mock_output_1 = [90, 80.0, 90.0, 100.0]
		self.assertEqual(self.reader.row_to_float(
			mock_input_1, rowcolheaders),mock_output_1)

	def test_row_to_float_E(self):
		rowcolheaders = False
		mock_input_1 = ["234",80,90,100]
		mock_output_1 = [234.0, 80.0, 90.0, 100.0]
		self.assertEqual(self.reader.row_to_float(
			mock_input_1, rowcolheaders),mock_output_1)




class TestGenerateDataGrid(unittest.TestCase):
	def setUp(self):
		self.path = "colorexlib/colorexlib/readers/tests/test_website_traffic.csv"
		self.reader = CSVReader(self.path, rowcol_headers=False)
		self.datagrid = self.reader.generate_datagrid()

	def test_generate_datagrid_A(self):
		mock_data = [
			["Month","Web Traffic","Call to actions"],
			["January",Data(100),Data(50)],
			["February",Data(1000),Data(900)],
			["March",Data(14500),Data(8000)],
			["April",Data(14500),Data(900)],
			["May",Data(9000),Data(12313)],
			["June",Data(15699),Data(54)],
			["July",Data(200456),Data(234)],
			["August",Data(34233),Data(512)],
			["September",Data(231231),Data(123)],
			["October",Data(128293),Data(543)],
			["November",Data(234234),Data(123)],
			["December",Data(111111),Data(445585)]
		]
		mock_datagrid = DataGrid({'data': mock_data})
		self.assertEqual(self.datagrid,
			mock_datagrid)