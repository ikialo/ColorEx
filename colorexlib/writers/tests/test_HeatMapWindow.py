import unittest
from colorexlib.colorexlib.writers.HeatMapWindow import HeatMapWindow
from colorexlib.colorexlib.common.datastructures import HeatMap, Data
from colorexlib.colorexlib.common.datastructures import DataGrid, Tile
from colorexlib.colorexlib.common.styling import StyleSheet
from colorexlib.colorexlib.common.styling import Theme
from tkinter import Tk


class TestInit(unittest.TestCase):
	def setUp(self):
		self.parent = Tk()

	def test___init__A(self):
		self.assertRaises(TypeError,HeatMapWindow)
		self.assertRaises(TypeError,HeatMapWindow,
			self.parent)

	def test___init__B(self):
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
		HeatMapWindow(self.parent, heatmap=heatmap)





@unittest.skip("Not necessary. Verified on screen.")
class TestOnMouseEnterTile(unittest.TestCase):
	pass


@unittest.skip("Not necessary. Verified on screen.")
class TestOnMouseLeaveTile(unittest.TestCase):
	pass


@unittest.skip("Not necessary. Verified on screen.")
class TestOnMouseClickTile(unittest.TestCase):
	pass


@unittest.skip("Not necessary. Verified on screen.")
class TestShowCurrentTileBalloon(unittest.TestCase):
	pass


@unittest.skip("Not necessary. Verified on screen.")
class TestHideAllTileBalloons(unittest.TestCase):
	pass


@unittest.skip("Not necessary. Verified on screen.")
class TestInitCanvas(unittest.TestCase):
	pass


@unittest.skip("Not necessary. Verified on screen.")
class TestCanvasCenterHeatmap(unittest.TestCase):
	pass



@unittest.skip("Not necessary. Verified on screen.")
class TestCanvasCenterHeader(unittest.TestCase):
	pass




@unittest.skip("Not necessary. Verified on screen.")
class TestCanvasGetNewPoint(unittest.TestCase):
	pass



@unittest.skip("Not necessary. Verified on screen.")
class TestCanvasDrawTile(unittest.TestCase):
	pass





@unittest.skip("Not necessary. Verified on screen.")
class TestCanvasDrawYaxisTick(unittest.TestCase):
	pass



@unittest.skip("Not necessary. Verified on screen.")
class TestCanvasDrawXaxisTick(unittest.TestCase):
	pass


@unittest.skip("Not necessary. Verified on screen.")
class TestCanvasUpdateScrollRegion(unittest.TestCase):
	pass



@unittest.skip("Not necessary. Verified on screen.")
class TestOnConfigure(unittest.TestCase):
	pass


@unittest.skip("Not necessary. Verified on screen.")
class TestRender(unittest.TestCase):
	pass



