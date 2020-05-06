import unittest
from ..HeatMapWindow import HeatMapWindow
from tkinter import Tk

from colorexlib.colorexlib.common.datastructures import HeatMap
from colorexlib.colorexlib.common.styling import StyleSheet

class TestInit(unittest.TestCase):
	def setUp(self):
		parent = Tk()
		stylesheet = StyleSheet()
		heatmap_options = dict()
		heatmap = HeatMap()

	def test___init__A(self):
		self.assertRaises(TypeError,HeatMapWindow)
		self.assertRaises(TypeError,HeatMapWindow,
			)