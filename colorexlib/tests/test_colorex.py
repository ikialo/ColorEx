'''

Copyright 2019 Louis Ronald

Permission is hereby granted, free of charge, to any person 
obtaining a copy of this software and associated documentation 
files (the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, 
publish, distribute, sublicense, and/or sell copies of the Software, 
and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be 
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES 
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
DEALINGS IN THE SOFTWARE.



'''

from ..colorex import CX_HeatMap
from ..common.datastructures import Data, DataGrid, Tile, HeatMap
import pytest


''' CX_HeatMap tests '''
options1 = dict()
options2 = dict()

options1['source'] = ['test_webtraffic_data.csv', 'csv']
options1['title'] = 'Website Traffic 2017'
options1['subtitle'] = 'The website traffic for whatever.com in the year 2017'

options2['source'] = ['test_webtraffic_data.csv', 'csv']
options2['title'] = 'Website Traffic 2017'
options2['subtitle'] = 'The website traffic for whatever.com in the year 2017'

data = [['Month', 'Web Traffic', 'Call to actions'],
        ['January', Data(100.0), Data(50.0)],
        ['February', Data(1000.0), Data(900.0)],
        ['March', Data(14500.0), Data(8000.0)],
        ['April', Data(14500.0), Data(900.0)],
        ['May', Data(9000.0), Data(12313.0)],
        ['June', Data(15699.0), Data(54.0)],
        ['July', Data(200456.0), Data(234.0)],
        ['August', Data(34233.0), Data(512.0)],
        ['September', Data(231231.0), Data(123.0)],
        ['October', Data(128293.0), Data(543.0)],
        ['November', Data(234234.0), Data(123.0)],
        ['December', Data(111111.0), Data(445585.0)]]
title = options1['title']
subtitle = options1['subtitle']


def test_CX_HeatMap_filename():
    cxg1 = CX_HeatMap(options1)
    assert cxg1.filename == options1['source'][0]

def test_CX_HeatMap_fileformat():
    cxg1 = CX_HeatMap(options1)
    assert cxg1.fileformat == options1['source'][1]

def test_CX_HeatMap_title():
    cxg1 = CX_HeatMap(options1)
    assert cxg1.title == options1['title']

def test_CX_HeatMap_subtitle():
    cxg1 = CX_HeatMap(options1)
    assert cxg1.subtitle == options1['subtitle']


def test_CX_HeatMap_theme():
    cxg1 = CX_HeatMap(options1)
    cxg2 = CX_HeatMap(options2)
    assert cxg1.theme == 'default'
    assert cxg2.theme == 'default'




def test_CX_HeatMap_generate_heatmap():
    cxg1 = CX_HeatMap(options1)
    data_grid = DataGrid({'data': data})
    heatmap = cxg1.generate_heatmap(data_grid)
    mock_heatmap = HeatMap({
        'data': data,
        'title': title,
        'subtitle': subtitle,
        'theme': cxg1.theme
    })
    assert heatmap == mock_heatmap


def test_CX_HeatMap_generate_tile():
    cxg1 = CX_HeatMap(options1)
    max_val = Data(90)
    data_item1 = Data(17.85)
    data_item2 = Data(0.9)
    
    assert cxg1.generate_tile(data_item1, max_val, '#ff0000') == Tile({'value': 17.85, 'alpha': 0.19833, 'rgb': '#ff0000'})
    assert cxg1.generate_tile(data_item2, max_val, '#ff0000') == Tile({'value': 0.9, 'alpha': 0.01, 'rgb': '#ff0000'})



def test_CX_HeatMap_calculate_rgb_alpha():
    cxg1 = CX_HeatMap(options1)
    max_val = Data(60)
    data_item1 = 43
    data_item2 = 98.8
    assert cxg1.calculate_rgb_alpha(data_item1, max_val) == 0.7166666666666667
    assert cxg1.calculate_rgb_alpha(data_item2, max_val) == 1.6466666666666667






def test_CX_HeatMap_to_html():
    # Test not implemented as success or failure of test
    # depends on creation of a HTML file.
    pass
