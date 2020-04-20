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


from .styling import Themes, Theme, StyleSheet



class Data:

    ''' Represents a single numeric data item in a data grid ''' 

    def __init__(self, value):
        self.__value = value
        if(not isinstance(value, int) and 
           not isinstance(value, float)):
            raise TypeError(str(value)+" is of invalid type. Must be of type \'int\' or \'float\'.")

    @property
    def value(self):
        ''' value of the data item '''
        return self.__value


    def __str__(self):
        return 'Data(' + str(self.__value) + ')'


    def __repr__(self):
        return 'Data(' + str(self.__value) + ')'


    def __lt__(self, data):
        if(self.__value < data.value):
            return True
        else:
            return False

    def __gt__(self, data):
        if(self.__value > data.value):
            return True
        else:
            return False


    def __le__(self, data):
        if(self.__value <= data.value):
            return True
        else:
            return False


    def __ge__(self, data):
        if(self.__value >= data.value):
            return True
        else:
            return False


    def __eq__(self, data):
        if(self.__value == data.value):
            return True
        else:
            return False










class Tile:

    ''' Represents a single tile in a grid of heat map tiles '''

    def __init__(self, options):
        '''Initialize a single Tile object '''

        # ensure validity of 'value' in options
        if('value' not in options):
            raise TypeError("required argument 'value' not specified")
        elif(not isinstance(options['value'], int) and 
            not isinstance(options['value'], float)):
            raise TypeError("argument 'value' must be of type 'int' or 'float'")


        # ensure validity of 'alpha' in options
        elif('alpha' not in options):
            raise TypeError("required argument 'alpha' not specified")
        elif(not isinstance(options['alpha'], int) and 
            not isinstance(options['alpha'], float)):
            raise TypeError("argument 'alpha' must be of type 'int' or 'float'")
        elif(options['alpha'] < 0 or options['alpha'] > 1):
            raise ValueError("argument 'alpha' must be between 0-1 inclusively")


        # ensure validity of 'rgb' in options
        elif('rgb' not in options):
            raise TypeError("required argument 'rgb' not specified")
        elif(not isinstance(options['rgb'], str)):
            raise TypeError("argument 'rgb' must be of type 'str'")

        elif(not Themes().is_rgb_hex(options['rgb'])):
            raise ValueError("argument 'rgb' must be between #000000 to #ffffff, and preceded with '#'")




        self.__value = options['value']
        self.__alpha = options['alpha']
        self.__rgb = options['rgb']
        self.__options = options



    @property
    def value(self):
        ''' get the value '''
        return self.__value
    
    @property
    def alpha(self):
        ''' get the alpha value '''
        return self.__alpha

    @property
    def rgb(self):
        ''' get the RGB hex color code '''
        return self.__rgb

    @property
    def options(self):
        ''' get tile options '''
        return self.__options

    @alpha.setter
    def alpha(self, value):
        ''' set the alpha value '''
        self.__alpha = value

    @rgb.setter
    def rgb(self, value):
        ''' set the rgb color code '''
        self.__rgb = value


    def __str__(self):
        return 'Tile(' + str(self.__options) + ')'


    def __repr__(self):
        return 'Tile(' + str(self.__options) + ')'


    def __lt__(self, tile):
        if(self.__value < tile.value):
            return True
        else:
            return False


    def __gt__(self, tile):
        if(self.__value > tile.value):
            return True
        else:
            return False


    def __le__(self, tile):
        if(self.__value <= tile.value):
            return True
        else:
            return False


    def __ge__(self, tile):
        if(self.__value >= tile.value):
            return True
        else:
            return False


    def __eq__(self, tile):
        if(self.__value == tile.value):
            return True
        else:
            return False

    





class DataGrid(object):

    def __init__(self, options):
        ''' Initialize DataGrid object '''

        # ensure arguments passed are valid.
        if('data' not in options):
            raise TypeError("required argument 'data' not specified")
        elif(not isinstance(options['data'],list)):
            raise TypeError("argument 'data' must be of type 'list', i.e. list of lists")
        for row in options['data']:
            if(not isinstance(row, list)):
                raise TypeError("argument 'data' must be of type 'list', i.e. list of lists")

        self.__grid = options['data']
        self.__size = self.__calculate_size(self.__grid)
        self.__shape = self.__calculate_shape(self.__grid)
        self.__rows = self.__shape['rows']
        self.__cols = self.__shape['cols']

        # determine if optional object parameters are passed.
        if('rowcol_headers' in options):
            self.__rowcolheaders = options['rowcol_headers']
        else:
            self.__rowcolheaders = True



    @property
    def grid(self):
        ''' Get data grid (list of lists) '''
        return self.__grid


    @property
    def size(self):
        ''' get the size of grid '''
        return self.__size


    @property
    def shape(self):
        ''' get the shape of grid '''
        return self.__shape

    @property
    def rows(self):
        ''' get the rows of grid '''
        return self.__rows

    @property
    def cols(self):
        ''' get the cols of grid '''
        return self.__cols


    @property
    def rowcolheaders(self):
        ''' are row and column headers set '''
        return self.__rowcolheaders



    def get_data(self, row, col):
        ''' get value by row, col '''
        item = self.__grid[row][col]
        return item




    def get_max_value(self):
        ''' get maximum value in the whole grid '''
        grid = self.__grid
        max_values = list()
        # determine start rows and columns 
        # given the 'rowcolheaders' option.
        if(self.__rowcolheaders):
            firstCol = 1
        else:
            firstCol = 0
        if(self.__rowcolheaders):
            firstRow = 1
        else:
            firstRow = 0

        # determine the maximum value in this
        # DataGrid object.
        for row in range(firstRow, len(grid)):
            row_max = list()
            for col in range(firstCol, len(grid[0])):
                try:
                    row_max.append(grid[row][col])
                except:
                    continue
            if(len(row_max)!=0):
                max_values.append(max(row_max))
        # return the maximum value.
        return max(max_values)


    
    
    def __calculate_size(self, grid):
        ''' calculates size of the grid '''
        size = 0
        for row in grid:
            size += len(row)
        return size



    def __calculate_shape(self, grid):
        ''' calculates the shape of the grid '''
        rows = 0
        cols = 0
        rows = len(grid)
        cols = len(grid[0])
        return {'rows': rows, 'cols': cols}

    

    def __str__(self):
        return 'DataGrid(' + str(self.__grid) + ')'



    def __repr__(self):
        return 'DataGrid(' + str(self.__grid) + ')'



    def __eq__(self, data_grid):
        if(self.__grid == data_grid.grid):
            return True
        else:
            return False







class HeatMap(object):

    

    def __init__(self, options):
        ''' Initialize HeatMap object '''

        # ensure validity of the arguments passed.
        if('data' not in options):
            raise TypeError("required argument 'data' not specified")
        elif(not isinstance(options['data'], list)):
            raise TypeError("argument 'data' must be of type 'list' (i.e. list of lists) and further contain items of type 'str' or 'Tile'")
        for row in options['data']:
            if(not isinstance(row, list)):
                raise TypeError("argument 'data' must be of type 'list' (i.e. list of lists) and further contain items of type 'str' or 'Tile'")
            else:
                for field in row:
                    if(not isinstance(field, str) and not isinstance(field, Tile)):
                        raise TypeError("argument 'data' must be of type 'list' (i.e. list of lists) and further contain items of type 'str' or 'Tile'")
        

        if('title' not in options):
            raise TypeError("required argument 'title' not specified")
        elif(not isinstance(options['title'], str)):
            raise TypeError("argument 'title' must be of type 'str'")
        elif('subtitle' not in options):
            raise TypeError("required argument 'subtitle' not specified")
        elif(not isinstance(options['subtitle'], str)):
            raise TypeError("argument 'subtitle' must be of type 'str'")
        elif('theme' not in options):
            raise TypeError("required argument 'theme' not specified")
        elif(not isinstance(options['theme'], Theme)):
            raise TypeError("argument 'theme' must be of type 'Theme'")
        elif('stylesheet' not in options):
            raise TypeError("required argument 'stylesheet' not specified")
        elif(not isinstance(options['stylesheet'], StyleSheet)):
            raise TypeError("argument 'stylesheet' must be of type 'StyleSheet'")
        elif('xaxis_title' not in options):
            raise TypeError("required argument 'xaxis_title' not specified")
        elif(not isinstance(options['xaxis_title'], str)):
            raise TypeError("argument 'xaxis_title' must be of type 'str'")
        elif('yaxis_title' not in options):
            raise TypeError("required argument 'yaxis_title' not specified")
        elif(not isinstance(options['yaxis_title'], str)):
            raise TypeError("argument 'yaxis_title' must be of type 'str'")


        self.__grid = options['data']
        self.__size = self.__calculate_size(self.__grid)
        self.__shape = self.__calculate_shape(self.__grid)
        self.__rows = self.__shape['rows']
        self.__cols = self.__shape['cols']
        self.__title = options['title']
        self.__subtitle = options['subtitle']
        self.__theme = options['theme']
        self.__stylesheet = options['stylesheet']
        self.__xaxistitle = options['xaxis_title']
        self.__yaxistitle = options['yaxis_title']

        # determine and set optional arguments passed
        if('xaxis_labels' in options):
            self.__xaxislabels = options['xaxis_labels']
        else:
            self.__xaxislabels = None
        if('yaxis_labels' in options):
            self.__yaxislabels = options['yaxis_labels']
        else:
            self.__yaxislabels = None
        if('theme' in options):
            self.__theme = options['theme']
        else:
            self.__theme = 'default'
        if('rowcol_headers' in options):
            self.__rowcolheaders = options['rowcol_headers']
        else:
            self.__rowcolheaders = True


    @property
    def grid(self):
        ''' get HeatMap data (list of lists) '''
        return self.__grid


    @property
    def size(self):
        ''' get size of heat map '''
        return self.__size

    @property
    def shape(self):
        ''' get shape of heat map '''
        return self.__shape

    @property
    def rows(self):
        ''' get number of rows in heat map '''
        return self.__rows

    @property
    def cols(self):
        ''' get number of cols in heat map '''
        return self.__cols


    @property
    def title(self):
        ''' get title of the heat map '''
        return self.__title


    @property
    def subtitle(self):
        ''' get subtitle of the heat map '''
        return self.__subtitle


    @property
    def theme(self):
        ''' get theme dictionary of options '''
        return self.__theme



    @property
    def stylesheet(self):
        ''' get stylesheet object of of style settings'''
        return self.__stylesheet


    @property
    def xaxistitle(self):
        ''' get the x-axis title'''
        return self.__xaxistitle


    @property
    def yaxistitle(self):
        ''' get the y-axis title '''
        return self.__yaxistitle



    @property
    def xaxislabels(self):
        ''' get the x-axis labels '''
        return self.__xaxislabels


    @property
    def yaxislabels(self):
        ''' get the y-axis labels '''
        return self.__yaxislabels


    @property
    def rowcolheaders(self):
        ''' is row and column headers set '''
        return self.__rowcolheaders



    def get_tile(self, row, col):
        ''' get a specific tile by row, column '''
        return self.__grid[row][col]



    def get_distinct_tiles(self):
        ''' returns a list of non-repeated tile values '''
        tiles = self.__grid
        list_of_values = list()
        # get all tile values into a list.
        for i in range(len(tiles)):
            for j in range(len(tiles[0])):
                try:
                    list_of_values.append(tiles[i][j].value)
                except:
                    continue
        # remove any repeated tile values, and leave
        # only one occurence of that repeated tile value.
        for i in range(len(list_of_values)):
            try:
                if(list_of_values.count(list_of_values[i]) > 1):
                    list_of_values.pop(i)
            except:
                continue
        # return list of non-repeated tile values
        return list_of_values
    


    def __calculate_size(self, grid):
        ''' calculate size of the heat map '''
        size = 0
        for row in grid:
            size += len(row)
        return size


    def __calculate_shape(self, grid):
        ''' calculate the shape of the heat map '''
        rows = 0
        cols = 0
        rows = len(grid)
        cols = len(grid[0])
        return {'rows': rows, 'cols': cols}



    def __str__(self):
        return 'HeatMap(' + str(self.__grid) + ')'



    def __repr__(self):
        return 'HeatMap(' + str(self.__grid) + ')'


    def __eq__(self, heat_map):
        if(self.__grid == heat_map):
            return True
        else:
            return False
