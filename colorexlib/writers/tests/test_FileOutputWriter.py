import unittest
from colorexlib.colorexlib.writers.FileOutputWriter import FileOutputWriter
from colorexlib.colorexlib.common.datastructures import HeatMap, Tile
from colorexlib.colorexlib.common.styling import Theme, StyleSheet

class TestInit(unittest.TestCase):

	def test___init__A(self):
		mock_data = [
			["Month","Web Traffic","Call to actions"],
			["January",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["February",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["March",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["April",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["May",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["June",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["July",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["August",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["September",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["October",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["November",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["December",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})]
		]
		options = {
			'data': mock_data,
			'title': 'My First Heatmap title',
			'subtitle': 'The first heatmap subtitle',
			'theme': Theme(),
			'stylesheet': StyleSheet(),
			'xaxis_title': 'Title of X-Axis',
			'yaxis_title': 'Title of Y-Axis'
		}
		heatmap = HeatMap(options)
		FileOutputWriter(filepath="filepath.file",heatmap=heatmap)



class TestFilePathGetter(unittest.TestCase):
	def test_file_path_getter_A(self):
		mock_data = [
			["Month","Web Traffic","Call to actions"],
			["January",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["February",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["March",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["April",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["May",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["June",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["July",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["August",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["September",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["October",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["November",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["December",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})]
		]
		options = {
			'data': mock_data,
			'title': 'My First Heatmap title',
			'subtitle': 'The first heatmap subtitle',
			'theme': Theme(),
			'stylesheet': StyleSheet(),
			'xaxis_title': 'Title of X-Axis',
			'yaxis_title': 'Title of Y-Axis'
		}
		heatmap = HeatMap(options)
		file_output_writer=FileOutputWriter(filepath="filepath.file",heatmap=heatmap)
		self.assertEqual(file_output_writer.filepath,
			"filepath.file")






class TestFilePathSetter(unittest.TestCase):
	def test_file_path_setter_A(self):
		mock_data = [
			["Month","Web Traffic","Call to actions"],
			["January",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["February",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["March",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["April",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["May",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["June",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["July",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["August",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["September",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["October",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["November",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["December",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})]
		]
		options = {
			'data': mock_data,
			'title': 'My First Heatmap title',
			'subtitle': 'The first heatmap subtitle',
			'theme': Theme(),
			'stylesheet': StyleSheet(),
			'xaxis_title': 'Title of X-Axis',
			'yaxis_title': 'Title of Y-Axis'
		}
		heatmap = HeatMap(options)
		file_output_writer=FileOutputWriter(filepath="filepath.file",heatmap=heatmap)
		self.assertEqual(file_output_writer.filepath,
			"filepath.file")
		file_output_writer.filepath = "myfile.html"
		self.assertEqual(file_output_writer.filepath,
			"myfile.html")






class TestHeatMapGetter(unittest.TestCase):
	def test_heatmap_getter_A(self):
		mock_data = [
			["Month","Web Traffic","Call to actions"],
			["January",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["February",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["March",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["April",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["May",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["June",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["July",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["August",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["September",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["October",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["November",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["December",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})]
		]
		options = {
			'data': mock_data,
			'title': 'My First Heatmap title',
			'subtitle': 'The first heatmap subtitle',
			'theme': Theme(),
			'stylesheet': StyleSheet(),
			'xaxis_title': 'Title of X-Axis',
			'yaxis_title': 'Title of Y-Axis'
		}
		heatmap = HeatMap(options)
		file_output_writer=FileOutputWriter(filepath="filepath.file",heatmap=heatmap)
		self.assertEqual(file_output_writer.heatmap,
			heatmap)




class TestHeatMapSetter(unittest.TestCase):
	def test_heatmap_setter_A(self):
		mock_data1 = [
			["Month","Web Traffic","Call to actions"],
			["January",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["February",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["March",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["April",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["May",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["June",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["July",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["August",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["September",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["October",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["November",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["December",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})]
		]
		mock_data2 = [
			["Month","Web Traffic","Call to actions"],
			["January",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["February",Tile({'value': 60.67, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["March",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["April",Tile({'value': 20, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 10, 'rgb': '#a45aff', 'alpha': 0.56})],
			["May",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.345})],
			["June",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 15.89, 'rgb': '#a45aff', 'alpha': 0.34})],
			["July",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["August",Tile({'value': 67.89, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["September",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.553})],
			["October",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.45}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.11})],
			["November",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.5}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.911})],
			["December",Tile({'value': 908, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.734})]
			]
		options1 = {
			'data': mock_data1,
			'title': 'My First Heatmap title',
			'subtitle': 'The first heatmap subtitle',
			'theme': Theme(),
			'stylesheet': StyleSheet(),
			'xaxis_title': 'Title of X-Axis',
			'yaxis_title': 'Title of Y-Axis'
		}
		options2 = {
			'data': mock_data2,
			'title': 'My First Heatmap title',
			'subtitle': 'The first heatmap subtitle',
			'theme': Theme(),
			'stylesheet': StyleSheet(),
			'xaxis_title': 'Title of X-Axis',
			'yaxis_title': 'Title of Y-Axis'
		}
		heatmap1 = HeatMap(options1)
		heatmap2 = HeatMap(options2)
		file_output_writer=FileOutputWriter(filepath="filepath.file",heatmap=heatmap1)
		self.assertEqual(file_output_writer.heatmap,
			heatmap1)
		file_output_writer.heatmap = heatmap2
		self.assertEqual(file_output_writer.heatmap,
			heatmap2)






class TestStyleSheetGetter(unittest.TestCase):
	def test_stylesheet_getter_A(self):
		mock_data = [
			["Month","Web Traffic","Call to actions"],
			["January",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["February",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["March",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["April",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["May",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["June",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["July",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["August",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["September",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["October",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["November",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["December",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})]
		]
		stylesheet = StyleSheet()
		options = {
			'data': mock_data,
			'title': 'My First Heatmap title',
			'subtitle': 'The first heatmap subtitle',
			'theme': Theme(),
			'stylesheet': stylesheet,
			'xaxis_title': 'Title of X-Axis',
			'yaxis_title': 'Title of Y-Axis'
		}
		heatmap = HeatMap(options)
		file_output_writer=FileOutputWriter(filepath="filepath.file",heatmap=heatmap)
		self.assertEqual(heatmap.stylesheet,
			stylesheet)





class TestStyleSheetSetter(unittest.TestCase):
	def test_stylesheet_setter_A(self):
		mock_data = [
			["Month","Web Traffic","Call to actions"],
			["January",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["February",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["March",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["April",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["May",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["June",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["July",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["August",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["September",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["October",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["November",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["December",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})]
		]
		stylesheet1 = StyleSheet()
		stylesheet2 = StyleSheet()
		options = {
			'data': mock_data,
			'title': 'My First Heatmap title',
			'subtitle': 'The first heatmap subtitle',
			'theme': Theme(),
			'stylesheet': stylesheet1,
			'xaxis_title': 'Title of X-Axis',
			'yaxis_title': 'Title of Y-Axis'
		}
		heatmap = HeatMap(options)
		file_output_writer=FileOutputWriter(filepath="filepath.file",heatmap=heatmap)
		self.assertEqual(file_output_writer.stylesheet,
			stylesheet1)
		file_output_writer.stylesheet = stylesheet2
		self.assertEqual(file_output_writer.stylesheet,
			stylesheet2)






class TestWrite(unittest.TestCase):
	def test_write_A(self):
		mock_data = [
			["Month","Web Traffic","Call to actions"],
			["January",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["February",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["March",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["April",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["May",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})]
		]
		stylesheet = StyleSheet()
		options = {
			'data': mock_data,
			'title': 'My First Heatmap title',
			'subtitle': 'The first heatmap subtitle',
			'theme': Theme(),
			'stylesheet': stylesheet,
			'xaxis_title': 'Title of X-Axis',
			'yaxis_title': 'Title of Y-Axis'
		}
		heatmap = HeatMap(options)
		file_output_writer=FileOutputWriter(filepath="filepath.file",heatmap=heatmap)
		self.assertRaises(NotImplementedError,
			file_output_writer.write)




