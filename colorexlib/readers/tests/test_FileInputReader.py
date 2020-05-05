import unittest
from colorexlib.colorexlib.readers.FileInputReader import FileInputReader


class TestInit(unittest.TestCase):


	def test___init__A(self):
		FileInputReader("C:\\users\\lronald\\desktop\\myfile.txt")
		FileInputReader("some string parameter")
	def test___init__B(self):
		self.assertRaises(TypeError,
			FileInputReader)
		self.assertRaises(TypeError,
			FileInputReader,
			8972)
		self.assertRaises(TypeError,
			FileInputReader,
			0x901)
		self.assertRaises(TypeError,
			FileInputReader,
			-1009)


class TestFilePathSetterGetter(unittest.TestCase):
	def setUp(self):
		self.filepath1 = "C:\\a_file"
		self.filepath2 = "C:\\Users\\lronald\\Desktop\\b_file"
		self.filepath3 = "C:\\Users\\lronald\\Documents\\c_file"
		self.fileInputReaderA = FileInputReader(self.filepath1)
		self.fileInputReaderB = FileInputReader(self.filepath2)
		self.fileInputReaderC = FileInputReader(self.filepath3)
	def test_filepath_A(self):
		self.assertEqual(self.fileInputReaderA.filepath,
			self.filepath1)
		self.fileInputReaderA.filepath = "new_file_path"
		self.assertNotEqual(self.fileInputReaderA.filepath,
			self.filepath1)


		self.assertEqual(self.fileInputReaderB.filepath,
			self.filepath2)
		self.fileInputReaderB.filepath = "new_file_path"
		self.assertNotEqual(self.fileInputReaderB.filepath,
			self.filepath2)


		self.assertEqual(self.fileInputReaderC.filepath,
			self.filepath3)
		self.fileInputReaderC.filepath = "new_file_path"
		self.assertNotEqual(self.fileInputReaderC.filepath,
			self.filepath3)
		






class TestDataSetterGetter(unittest.TestCase):
	def setUp(self):
		self.filepath1 = "C:\\a_file"
		self.filepath2 = "C:\\Users\\lronald\\Desktop\\b_file"
		self.filepath3 = "C:\\Users\\lronald\\Documents\\c_file"
		self.fileInputReaderA = FileInputReader(self.filepath1)
		self.fileInputReaderB = FileInputReader(self.filepath2)
		self.fileInputReaderC = FileInputReader(self.filepath3)
		self.data1 = [1,4,5,6]
		self.data2 = [9,1,56,3,-4]
		self.data3 = [10,5,6,4]
	def test_data_A(self):
		self.fileInputReaderA.data = self.data1
		self.assertEqual(self.fileInputReaderA.data,
			self.data1)

		self.fileInputReaderB.data = self.data2
		self.assertEqual(self.fileInputReaderB.data,
			self.data2)

		self.fileInputReaderC.data = self.data3
		self.assertEqual(self.fileInputReaderC.data,
			self.data3)




@unittest.skip("Method implemented by child class.")
class TestRead(unittest.TestCase):
	pass




@unittest.skip("Method implemented by child class.")
class TestGenerateDataGrid(unittest.TestCase):
	pass



