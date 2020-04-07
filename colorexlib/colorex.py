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
from .common.themes import Theme, Themes
from .common.datastructures import Data, HeatMap, DataGrid, Tile
from .writers.HTMLWriter import HTMLWriter
from .readers.CSVReader import CSVReader
import re

class CX_HeatMap:



    def __init__(self, options=dict()):
        ''' Initialize a new engine '''

        self.__filename = ""
        self.__fileformat = ""

        self.__filename = options["source"][0]
        self.__fileformat = options["source"][1]
        self.__title = options["title"]
        self.__subtitle = options["subtitle"]
        try:
            # If theme was specified
            self.__theme = options['theme']
        except:
            # If theme wasn't specified.
            self.__theme = 'default'

        self.__colors = Themes().colors
        self.__themes = Themes().themes


    @property
    def filename(self):
        ''' get the filename for output heat map '''
        return self.__filename

    @property
    def fileformat(self):
        ''' get the file format of output heat map '''
        return self.__fileformat

    @property
    def title(self):
        ''' get the title '''
        return self.__title

    @property
    def subtitle(self):
        ''' get the subtitle '''
        return self.__subtitle


    @property
    def theme(self):
        ''' get the currently set theme name '''
        return self.__theme



    def generate_heatmap(self, data_grid):
        ''' creates an object of type HeatMap '''
        new_data = list()
        max_values = data_grid.calculate_max_values_by_cols()
        heatmap = list()
        heatmap.append(data_grid.grid[0])
        
        for row in data_grid.grid[1:]:
            final_row = list()
            rgb_index = 0
            for item in range(len(row)):
                if(type(row[item]) is Data):

                    # We're just dealing with a theme here.
                    new_tile = self.generate_tile(row[item],
                        max_values[item],
                        self.__themes[self.__theme]['primary'])
                    final_row.append(new_tile)
                    rgb_index += 1
                    
                else:
                    final_row.append(row[item])
            heatmap.append(final_row)
            
        heatmap_obj = HeatMap({'data': heatmap,
            'title': self.__title,
            'subtitle': self.__subtitle,
            'theme': self.__themes[self.__theme]})

        return heatmap_obj

 
        
    def generate_tile(self, data_item, max_value, rgb):
        ''' generates a new tile of type Tile '''
        tile_options = {
                'value': data_item.value,
                'alpha': self.calculate_rgb_alpha(
                    data_item.value,
                    max_value),
                'rgb': Themes().rgb_hex_to_decimal(rgb)
        }
        return Tile(tile_options)



    def calculate_rgb_alpha(self, data_item, max_value):
        ''' calculates the alpha value for rgb color given
            data object and max value '''
        alpha_value = data_item / max_value.value
        return alpha_value



    def to_html(self, html_filename, template):
        ''' outputs HeatMap object to a HTML file '''
        if(self.__fileformat.lower() == 'csv'):
            reader = CSVReader(self.__filename)
            data_grid = reader.generate_datagrid()
            heat_map = self.generate_heatmap(data_grid)
            html_writer = HTMLWriter(html_filename, heat_map)
            html_writer.write({'template': template})
        else:
            raise Exception

