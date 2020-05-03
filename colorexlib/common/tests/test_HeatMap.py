import unittest
from ..datastructures import HeatMap
from ..datastructures import Tile
from ..styling import Theme, StyleSheet


class TestInit(unittest.TestCase):
	def test___init__A(self):
		options = dict()
		options['title'] = "A Title"
		options['subtitle'] = "A Subtitle"
		options['theme'] = Theme()
		options['stylesheet'] = StyleSheet()
		options['xaxis_title'] = 'XAxis Title'
		options['yaxis_title'] = 'YAxis Title'

		# declare some mock tiles.
		t1 = Tile({'value': 105, 'alpha': 0.45, 'rgb': '#f00000'})
		t2 = Tile({'value': 10, 'alpha': 0.2566, 'rgb': '#f10000'})
		t3 = Tile({'value': 123, 'alpha': 0.89, 'rgb': '#f20000'})
		t4 = Tile({'value': 45, 'alpha': 0.15, 'rgb': '#f30000'})
		t5 = Tile({'value': 35, 'alpha': 0.97, 'rgb': '#f40000'})
		t6 = Tile({'value': 89, 'alpha': 0.24, 'rgb': '#f50000'})
		t7 = Tile({'value': 67.43, 'alpha': 0.522, 'rgb': '#f60000'})
		t8 = Tile({'value': 49, 'alpha': 0.567, 'rgb': '#f70000'})
		t9 = Tile({'value': 100, 'alpha': 0.11, 'rgb': '#f80000'})

		options['data'] = [
			['',			'Monday',	'Tuesday',	'Wednesday'],
			['Morning',		t1, 		t2, 				t3],
			['Midday', 		t4, 		t5, 				t6],
			['Afternoon',	t7, 		t8, 				t9],
		]

		heatmap = HeatMap(options)


	def test___init__B(self):
		options = dict()
		options['title'] = "A Title"
		options['subtitle'] = "A Subtitle"
		options['theme'] = Theme()
		options['stylesheet'] = StyleSheet()
		#options['xaxis_title'] = 'XAxis Title'
		#options['yaxis_title'] = 'YAxis Title'

		# declare some mock tiles.
		t1 = Tile({'value': 105, 'alpha': 0.45, 'rgb': '#f00000'})
		t2 = Tile({'value': 10, 'alpha': 0.2566, 'rgb': '#f10000'})
		t3 = Tile({'value': 123, 'alpha': 0.89, 'rgb': '#f20000'})
		t4 = Tile({'value': 45, 'alpha': 0.15, 'rgb': '#f30000'})
		t5 = Tile({'value': 35, 'alpha': 0.97, 'rgb': '#f40000'})
		t6 = Tile({'value': 89, 'alpha': 0.24, 'rgb': '#f50000'})
		t7 = Tile({'value': 67.43, 'alpha': 0.522, 'rgb': '#f60000'})
		t8 = Tile({'value': 49, 'alpha': 0.567, 'rgb': '#f70000'})
		t9 = Tile({'value': 100, 'alpha': 0.11, 'rgb': '#f80000'})

		options['data'] = [
			['',			'Monday',	'Tuesday',	'Wednesday'],
			['Morning',		t1, 		t2, 				t3],
			['Midday', 		t4, 		t5, 				t6],
			['Afternoon',	t7, 		t8, 				t9],
		]

		self.assertRaises(TypeError,
			HeatMap,options)



@unittest.skip("Not necessary to test at the moment")
class TestGrid(unittest.TestCase):
	pass

@unittest.skip("Not necessary to test at the moment")
class TestSize(unittest.TestCase):
	pass

@unittest.skip("Not necessary to test at the moment")
class TestShape(unittest.TestCase):
	pass

@unittest.skip("Not necessary to test at the moment")
class TestRows(unittest.TestCase):
	pass

@unittest.skip("Not necessary to test at the moment")
class TestCols(unittest.TestCase):
	pass

@unittest.skip("Not necessary to test at the moment")
class TestTitle(unittest.TestCase):
	pass

@unittest.skip("Not necessary to test at the moment")
class TestSubtitle(unittest.TestCase):
	pass

@unittest.skip("Not necessary to test at the moment")
class TestTheme(unittest.TestCase):
	pass

@unittest.skip("Not necessary to test at the moment")
class TestStyleSheet(unittest.TestCase):
	pass

@unittest.skip("Not necessary to test at the moment")
class TestXAxisTitle(unittest.TestCase):
	pass

@unittest.skip("Not necessary to test at the moment")
class TestYAxisTitle(unittest.TestCase):
	pass

@unittest.skip("Not necessary to test at the moment")
class TestXAxisLabels(unittest.TestCase):
	pass

@unittest.skip("Not necessary to test at the moment")
class TestYAxisLabels(unittest.TestCase):
	pass

@unittest.skip("Not necessary to test at the moment")
class TestRowColHeaders(unittest.TestCase):
	pass

@unittest.skip("Not necessary to test at the moment")
class TestDataFormatter(unittest.TestCase):
	pass

@unittest.skip("Not necessary to test at the moment")
class TestGrouping(unittest.TestCase):
	pass


class TestGetTile(unittest.TestCase):
	def setUp(self):
		self.options = dict()
		self.options['title'] = "A Title"
		self.options['subtitle'] = "A Subtitle"
		self.options['theme'] = Theme()
		self.options['stylesheet'] = StyleSheet()
		self.options['xaxis_title'] = 'XAxis Title'
		self.options['yaxis_title'] = 'YAxis Title'
		# declare some mock tiles.
		self.t1 = Tile({'value': 105, 'alpha': 0.45, 'rgb': '#f00000'})
		self.t2 = Tile({'value': 10, 'alpha': 0.2566, 'rgb': '#f10000'})
		self.t3 = Tile({'value': 123, 'alpha': 0.89, 'rgb': '#f20000'})
		self.t4 = Tile({'value': 45, 'alpha': 0.15, 'rgb': '#f30000'})
		self.t5 = Tile({'value': 35, 'alpha': 0.97, 'rgb': '#f40000'})
		self.t6 = Tile({'value': 89, 'alpha': 0.24, 'rgb': '#f50000'})
		self.t7 = Tile({'value': 67.43, 'alpha': 0.522, 'rgb': '#f60000'})
		self.t8 = Tile({'value': 49, 'alpha': 0.567, 'rgb': '#f70000'})
		self.t9 = Tile({'value': 100, 'alpha': 0.11, 'rgb': '#f80000'})
		self.options['data'] = [
			['',			'Monday',	'Tuesday',	'Wednesday'],
			['Morning',		self.t1, 	self.t2, 	self.t3],
			['Midday', 		self.t4, 	self.t5, 	self.t6],
			['Afternoon',	self.t7, 	self.t8, 	self.t9],
		]
		self.heatmap = HeatMap(self.options)


	def test_get_tile_A(self):
		self.assertEqual(
			self.heatmap.get_tile(0,0),
			'')
		self.assertEqual(
			self.heatmap.get_tile(1,0),
			'Morning')
		self.assertEqual(
			self.heatmap.get_tile(2,0),
			'Midday')
		self.assertEqual(
			self.heatmap.get_tile(2,1),
			self.t4)
		self.assertEqual(
			self.heatmap.get_tile(3,2),
			self.t8)



	def test_get_tile_B(self):
		self.assertRaises(
			IndexError,
			self.heatmap.get_tile,
			5,0)
		self.assertRaises(
			IndexError,
			self.heatmap.get_tile,
			100,0)
		self.assertRaises(
			IndexError,
			self.heatmap.get_tile,
			0,4)




class TestGetDistinctTiles(unittest.TestCase):
	def setUp(self):
		self.options = dict()
		self.options['title'] = "A Title"
		self.options['subtitle'] = "A Subtitle"
		self.options['theme'] = Theme()
		self.options['stylesheet'] = StyleSheet()
		self.options['xaxis_title'] = 'XAxis Title'
		self.options['yaxis_title'] = 'YAxis Title'
		# declare some mock tiles.
		self.t1 = Tile({'value': 105, 'alpha': 0.45, 'rgb': '#f00000'})
		self.t2 = Tile({'value': 10, 'alpha': 0.2566, 'rgb': '#f10000'})
		self.t3 = Tile({'value': 123, 'alpha': 0.89, 'rgb': '#f20000'})
		self.t4 = Tile({'value': 45, 'alpha': 0.15, 'rgb': '#f30000'})
		self.t5 = Tile({'value': 45, 'alpha': 0.15, 'rgb': '#f30000'})
		self.t6 = Tile({'value': 89, 'alpha': 0.24, 'rgb': '#f50000'})
		self.t7 = Tile({'value': 89, 'alpha': 0.24, 'rgb': '#f50000'})
		self.t8 = Tile({'value': 89, 'alpha': 0.24, 'rgb': '#f50000'})
		self.t9 = Tile({'value': 100, 'alpha': 0.11, 'rgb': '#f80000'})
		self.options['data'] = [
			['',			'Monday',	'Tuesday',	'Wednesday'],
			['Morning',		self.t1, 	self.t2, 	self.t3],
			['Midday', 		self.t4, 	self.t5, 	self.t6],
			['Afternoon',	self.t7, 	self.t8, 	self.t9],
		]
		self.heatmap = HeatMap(self.options)

	def test_get_distinct_tiles_A(self):
		distinct_tiles = self.heatmap.get_distinct_tiles()
		the_tiles = [self.t1.value, self.t2.value, self.t3.value,
			self.t4.value,self.t6.value, self.t9.value]
		self.assertEqual(distinct_tiles, the_tiles)


@unittest.skip("Not necessary as it is a private method")
class TestCalculateSize(unittest.TestCase):
	pass

@unittest.skip("Not necessary as it is a private method")
class TestCalculateShape(unittest.TestCase):
	pass


class TestStr(unittest.TestCase):
	def setUp(self):
		self.options = dict()
		self.options['title'] = "A Title"
		self.options['subtitle'] = "A Subtitle"
		self.options['theme'] = Theme()
		self.options['stylesheet'] = StyleSheet()
		self.options['xaxis_title'] = 'XAxis Title'
		self.options['yaxis_title'] = 'YAxis Title'
		# declare some mock tiles.
		self.t1 = Tile({'value': 105, 'alpha': 0.45, 'rgb': '#f00000'})
		self.t2 = Tile({'value': 10, 'alpha': 0.2566, 'rgb': '#f10000'})
		self.t3 = Tile({'value': 123, 'alpha': 0.89, 'rgb': '#f20000'})
		self.t4 = Tile({'value': 45, 'alpha': 0.15, 'rgb': '#f30000'})
		self.t5 = Tile({'value': 45, 'alpha': 0.15, 'rgb': '#f30000'})
		self.t6 = Tile({'value': 89, 'alpha': 0.24, 'rgb': '#f50000'})
		self.t7 = Tile({'value': 89, 'alpha': 0.24, 'rgb': '#f50000'})
		self.t8 = Tile({'value': 89, 'alpha': 0.24, 'rgb': '#f50000'})
		self.t9 = Tile({'value': 100, 'alpha': 0.11, 'rgb': '#f80000'})
		self.options['data'] = [
			['',			'Monday',	'Tuesday',	'Wednesday'],
			['Morning',		self.t1, 	self.t2, 	self.t3],
			['Midday', 		self.t4, 	self.t5, 	self.t6],
			['Afternoon',	self.t7, 	self.t8, 	self.t9],
		]
		self.heatmap = HeatMap(self.options)
	def test___str__A(self):
		self.assertEqual(self.heatmap.__str__(),
			"HeatMap("+str(self.options['data'])
			+")")




class TestRepr(unittest.TestCase):
	def setUp(self):
		self.options = dict()
		self.options['title'] = "A Title"
		self.options['subtitle'] = "A Subtitle"
		self.options['theme'] = Theme()
		self.options['stylesheet'] = StyleSheet()
		self.options['xaxis_title'] = 'XAxis Title'
		self.options['yaxis_title'] = 'YAxis Title'
		# declare some mock tiles.
		self.t1 = Tile({'value': 105, 'alpha': 0.45, 'rgb': '#f00000'})
		self.t2 = Tile({'value': 10, 'alpha': 0.2566, 'rgb': '#f10000'})
		self.t3 = Tile({'value': 123, 'alpha': 0.89, 'rgb': '#f20000'})
		self.t4 = Tile({'value': 45, 'alpha': 0.15, 'rgb': '#f30000'})
		self.t5 = Tile({'value': 45, 'alpha': 0.15, 'rgb': '#f30000'})
		self.t6 = Tile({'value': 89, 'alpha': 0.24, 'rgb': '#f50000'})
		self.t7 = Tile({'value': 89, 'alpha': 0.24, 'rgb': '#f50000'})
		self.t8 = Tile({'value': 89, 'alpha': 0.24, 'rgb': '#f50000'})
		self.t9 = Tile({'value': 100, 'alpha': 0.11, 'rgb': '#f80000'})
		self.options['data'] = [
			['',			'Monday',	'Tuesday',	'Wednesday'],
			['Morning',		self.t1, 	self.t2, 	self.t3],
			['Midday', 		self.t4, 	self.t5, 	self.t6],
			['Afternoon',	self.t7, 	self.t8, 	self.t9],
		]
		self.heatmap = HeatMap(self.options)
	def test___repr__A(self):
		self.assertEqual(self.heatmap.__repr__(),
			"HeatMap("+repr(self.options['data'])
			+")")




class TestEqual(unittest.TestCase):
	def setUp(self):
		self.options1 = dict()
		self.options1['title'] = "A Title"
		self.options1['subtitle'] = "A Subtitle"
		self.options1['theme'] = Theme()
		self.options1['stylesheet'] = StyleSheet()
		self.options1['xaxis_title'] = 'XAxis Title'
		self.options1['yaxis_title'] = 'YAxis Title'

		self.options2 = dict()
		self.options2['title'] = "A Title"
		self.options2['subtitle'] = "A Subtitle"
		self.options2['theme'] = Theme()
		self.options2['stylesheet'] = StyleSheet()
		self.options2['xaxis_title'] = 'XAxis Title'
		self.options2['yaxis_title'] = 'YAxis Title'

		self.options3 = dict()
		self.options3['title'] = "A Title"
		self.options3['subtitle'] = "A Subtitle"
		self.options3['theme'] = Theme()
		self.options3['stylesheet'] = StyleSheet()
		self.options3['xaxis_title'] = 'XAxis Title'
		self.options3['yaxis_title'] = 'YAxis Title'


		# declare some mock tiles.
		self.t1 = Tile({'value': 105, 'alpha': 0.45, 'rgb': '#f00000'})
		self.t2 = Tile({'value': 10, 'alpha': 0.2566, 'rgb': '#f10000'})
		self.t3 = Tile({'value': 123, 'alpha': 0.89, 'rgb': '#f20000'})
		self.t4 = Tile({'value': 45, 'alpha': 0.15, 'rgb': '#f30000'})
		self.t5 = Tile({'value': 45, 'alpha': 0.15, 'rgb': '#f30000'})
		self.t6 = Tile({'value': 89, 'alpha': 0.24, 'rgb': '#f50000'})
		self.t7 = Tile({'value': 89, 'alpha': 0.24, 'rgb': '#f50000'})
		self.t8 = Tile({'value': 89, 'alpha': 0.24, 'rgb': '#f50000'})
		self.t9 = Tile({'value': 100, 'alpha': 0.11, 'rgb': '#f80000'})

		# create some data lists.
		self.data1 = [
			['',			'Monday',	'Tuesday',	'Wednesday'],
			['Morning',		self.t1, 	self.t2, 	self.t3],
			['Midday', 		self.t4, 	self.t5, 	self.t6],
			['Afternoon',	self.t7, 	self.t8, 	self.t9],
		]

		self.data2 = [
			['',			'Monday',	'Tuesday',	'Wednesday'],
			['Morning',		self.t4, 	self.t2, 	self.t3],
			['Midday', 		self.t1, 	self.t5, 	self.t6],
			['Afternoon',	self.t6, 	self.t8, 	self.t1],
		]


		self.data3 = [
			['',			'Monday',	'Tuesday',	'Wednesday'],
			['Morning',		self.t1, 	self.t2, 	self.t3],
			['Midday', 		self.t4, 	self.t5, 	self.t6],
			['Afternoon',	self.t7, 	self.t8, 	self.t9],
		]


		self.options1['data'] = self.data1
		self.options2['data'] = self.data2
		self.options3['data'] = self.data3

		self.heatmap1 = HeatMap(self.options1)
		self.heatmap2 = HeatMap(self.options2)
		self.heatmap3 = HeatMap(self.options3)

	def test___eq__A(self):
		self.assertFalse(self.heatmap1.__eq__(self.heatmap2))
		self.assertFalse(self.heatmap2.__eq__(self.heatmap3))
		self.assertTrue(self.heatmap1.__eq__(self.heatmap3))

	def test___eq__B(self):
		self.assertNotEqual(self.heatmap1, self.heatmap2)
		self.assertNotEqual(self.heatmap2, self.heatmap3)
		self.assertEqual(self.heatmap1, self.heatmap3)

