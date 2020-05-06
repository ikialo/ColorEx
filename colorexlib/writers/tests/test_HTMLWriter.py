from colorexlib.colorexlib.writers.HTMLWriter import HTMLWriter
from colorexlib.colorexlib.common.datastructures import Tile
from colorexlib.colorexlib.common.datastructures import HeatMap
from colorexlib.colorexlib.common.styling import Theme
from colorexlib.colorexlib.common.styling import StyleSheet
from Cheetah.Template import Template
import unittest
import os


class TestInit(unittest.TestCase):
	def test___init__A(self):
		mock_data = [
			["Month","Web Traffic","Call to actions"],
			["January",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),
				Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["February",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),
				Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["March",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),
				Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["April",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),
				Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["May",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),
				Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})]
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
		filepath = "myfilepath.html"
		heatmap = HeatMap(options)
		

		html_writer = HTMLWriter(filepath=filepath, heatmap=heatmap)

		self.assertRaises(TypeError, HTMLWriter, filepath=filepath,
			heatmap=list())








class TestWrite(unittest.TestCase):
	def test_write_A(self):
		mock_data = [
			["Month","Web Traffic","Call to actions"],
			["January",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),
				Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["February",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),
				Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["March",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),
				Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["April",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),
				Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
			["May",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),
				Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})]
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
		filepath = "myoutputfile.html"
		heatmap = HeatMap(options)
		html_writer = HTMLWriter(filepath=filepath, heatmap=heatmap)
		html_writer.write()
		self.assertTrue(os.path.exists(filepath))
		os.remove(filepath)










# class TestGenerateHtmlTemplateStr(unittest.TestCase):
# 	def test_generate_html_template_str(self):
# 		mock_data = [
# 			["Month","Web Traffic","Call to actions"],
# 			["January",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),
# 				Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
# 			["February",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),
# 				Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
# 			["March",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),
# 				Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
# 			["April",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),
# 				Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})],
# 			["May",Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56}),
# 				Tile({'value': 60, 'rgb': '#a45aff', 'alpha': 0.56})]
# 		]
# 		stylesheet = StyleSheet()
# 		options = {
# 			'data': mock_data,
# 			'title': 'My First Heatmap title',
# 			'subtitle': 'The first heatmap subtitle',
# 			'theme': Theme(),
# 			'stylesheet': stylesheet,
# 			'xaxis_title': 'Title of X-Axis',
# 			'yaxis_title': 'Title of Y-Axis'
# 		}
# 		filepath = "myoutputfile.html"
# 		heatmap = HeatMap(options)
# 		html_writer = HTMLWriter(filepath=filepath, heatmap=heatmap)
# 		the_template_str = html_writer.generate_html_template_str()
# 		yaxis_labels = mock_data[0]
# 		xaxis_labels = list(map(lambda row: row[0], mock_data))
# 		heatmap_data = list(map(lambda row: row[1:], heatmap.grid[1:]))
# 		print("\n\n\n\n",heatmap_data,"\n\n\n\n")
# 		the_html_output = Template(the_template_str,
# 			searchList=[{'heatmap': heatmap,
# 						'data': heatmap_data,
# 						'yaxis_labels': yaxis_labels,
# 						'xaxis_labels': xaxis_labels,
# 						'title': heatmap.title,
# 						'subtitle': heatmap.subtitle,
# 						'theme': heatmap.theme,
# 						'stylesheet': heatmap.stylesheet}])
# 		the_html_output = str(the_html_output)



