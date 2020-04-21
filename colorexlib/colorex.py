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


# import necessary modules
from .common.styling import Theme, Themes, StyleSheet
from .common.datastructures import Data, HeatMap, DataGrid, Tile
from .writers.HTMLWriter import HTMLWriter
from .writers.GUIOutputWriter import GUIOutputWriter
from .readers.CSVReader import CSVReader
import re




class CX_HeatMap:



    def __init__(self, options=dict()):
        ''' Initialize a new engine '''
        
        # determine data input source type and source
        self.__source = options["source"]
        self.__sourcetype = ""
        # check if source is a filename
        if(isinstance(self.__source,str) and len(
            self.__source.split('.'))>1):
            # check what type of file it is based on file 
            # type suffix '.'
            filetype = self.__source.split('.')[-1]
            if(filetype == "csv"):
                self.__sourcetype = "csv"
            else:
                raise Exception
        # check if source is a data grid
        elif(isinstance(self.__source, DataGrid)):
            self.__sourcetype = 'datagrid'

        else:
            # the source is not supported so raise exception.
            raise Exception


        # set title and subtitle values
        self.__title = options["title"]
        self.__subtitle = options["subtitle"]



        # set the optional arguments and their values.
        # theme settings
        if('theme' in options):
            self.__theme = options["theme"]
        else:
            self.__theme = Theme()

        # stylesheet settings
        if('stylesheet' in options):
            self.__stylesheet = options["stylesheet"]
        else:
            self.__stylesheet = StyleSheet()

        # xaxis_title settings
        if("xaxis_title" in options):
            self.__xaxistitle = options["xaxis_title"]
        else:
            self.__xaxistitle = ""

        # yaxis_title settings
        if("yaxis_title" in options):
            self.__yaxistitle = options["yaxis_title"]
        else:
            self.__yaxistitle = ""

        # xaxis_labels settings
        if("xaxis_labels" in options):
            self.__xaxislabels = options['xaxis_labels']
        else:
            self.__xaxislabels = None

        # yaxis_labels settings
        if("yaxis_labels" in options):
            self.__yaxislabels = options['yaxis_labels']
        else:
            self.__yaxislabels = None

        # rowcol_headers settings
        if("rowcol_headers" in options):
            self.__rowcolheaders = options["rowcol_headers"]
        else:
            self.__rowcolheaders = True


        # set dictionary of available colors and themes
        # for reference.
        self.__colors = Themes().colors
        self.__themes = Themes().themes



    @property
    def source(self):
        ''' get the data source '''
        return self.__source


    @property
    def sourcetype(self):
        ''' get the data source type '''
        return self.__sourcetype



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

    @property
    def stylesheet(self):
        ''' get the currently set stylesheet object '''
        return self.__stylesheet


    @property
    def xaxistitle(self):
        ''' get the x-axis label'''
        return self.__xaxistitle


    @property
    def yaxistitle(self):
        ''' get the y-axis label '''
        return self.__yaxistitle


    @property
    def rowcolheaders(self):
        ''' get whether row column headers are set 
        in the data source '''
        return self.__rowcolheaders




    def generate_heatmap(self, data_grid):
        ''' creates an object of type HeatMap '''
        new_data = list()
        # get the maximum value out of the
        # entire DataGrid object passed.
        max_value = data_grid.get_max_value()
        heatmap = list()
        grid = data_grid.grid
        # generate a heatmap Tile for every
        # data item detected as 'Data' type
        # from the passed DataGrid object
        for row in grid:
            final_row = list()
            for item in range(len(row)):
                if(type(row[item]) is Data):                    
                    new_tile = self.generate_tile(row[item],
                        max_value,
                        self.__theme)
                    final_row.append(new_tile)
                else:
                    final_row.append(row[item])
            heatmap.append(final_row)
        # create a HeatMap object passing options
        # and especially the DataGrid object.
        heatmap_obj = HeatMap({'data': heatmap,
            'title': self.__title,
            'subtitle': self.__subtitle,
            'theme': self.__theme,
            'stylesheet': self.__stylesheet,
            'xaxis_title': self.__xaxistitle,
            'yaxis_title': self.__yaxistitle,
            'rowcol_headers': data_grid.rowcolheaders,
            'xaxis_labels': self.__xaxislabels,
            'yaxis_labels': self.__yaxislabels})
        return heatmap_obj

 


        
    def generate_tile(self, data_item, max_value, theme):
        ''' generates a new tile of type Tile '''
        # set some colors to use.
        highColor = theme.palette["primary"]
        lowColor = theme.palette["secondary"]
        highColorDec = Themes().rgb_hex_to_decimal(highColor)
        lowColorDec = Themes().rgb_hex_to_decimal(lowColor)
        alpha_color = Themes().generate_alpha_rgb_bicolor(
            highColorDec,lowColorDec,self.calculate_rgb_alpha(
                data_item.value, max_value))
        rgb = Themes().decimal_to_rgb_hex(alpha_color)
        # create a dictionary for all Tile options.
        tile_options = {
                'value': data_item.value,
                'alpha': self.calculate_rgb_alpha(
                    data_item.value,
                    max_value),
                'rgb': rgb
        }
        # return a Tile object, passing the options too.
        return Tile(tile_options)




    def calculate_rgb_alpha(self, data_item, max_value):
        ''' calculates the alpha value for rgb color given
            data object and max value '''
        alpha_value = data_item / max_value.value
        return alpha_value




    def to_html(self, html_filename, template):
        ''' outputs HeatMap object to a HTML file '''

        # Determine the source of the input data
        if(self.__sourcetype.lower() == 'csv'):
            # CSV file is the input source.
            reader = CSVReader(self.__source, self.__skip_first_row, 
                self.__skip_first_column)
            data_grid = reader.generate_datagrid()
            heat_map = self.generate_heatmap(data_grid)
            stylesheet = self.stylesheet
            html_writer = HTMLWriter(filepath=html_filename, 
                heatmap=heat_map, stylesheet=stylesheet)
            html_writer.write({'template': template})

        else:
            # the source is not supported so raise exception.
            raise Exception


    
    def to_gui(self):

        ''' outputs HeatMap to a GUI screen'''

        # Determine ths oruce of the input data
        if(self.__sourcetype.lower() == 'csv'):
            # CSV file is the input source.
            reader = CSVReader(self.__source, self.__rowcolheaders)
            data_grid = reader.generate_datagrid()
            heat_map = self.generate_heatmap(data_grid)
            gui_writer = GUIOutputWriter(heatmap=heat_map,
                stylesheet=self.__stylesheet)
            gui_writer.write()

        elif(self.__sourcetype.lower() == 'datagrid'):
            # DataGrid object is the input source
            data_grid = self.__source
            heat_map = self.generate_heatmap(data_grid)
            gui_writer = GUIOutputWriter(heatmap=heat_map,
                stylesheet=self.__stylesheet)
            gui_writer.write()

        else:
            # the source is not supported so raise exception.
            raise Exception

