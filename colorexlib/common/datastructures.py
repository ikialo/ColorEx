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


#from .styling import Themes, Theme, StyleSheet
from colorexlib.colorexlib.common.styling import Themes, Theme, StyleSheet


class Data:

    ''' Represents a single numeric data item in a data grid ''' 

    def __init__(self, value):
        self.__value = value
        if(not isinstance(value, int) and 
           not isinstance(value, float)):
            raise TypeError(str(value)+" is of invalid type. \
                Must be of type 'int' or 'float'.")

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


        # ensure options passed is a dictionary
        if(not isinstance(options, dict)):
            raise TypeError("required argument 'options' must be of type 'dict'")


        # ensure validity of 'value' in options
        if('value' not in options):
            raise TypeError("required argument 'value' \
                not specified")
        elif(not isinstance(options['value'], int) and 
            not isinstance(options['value'], float)):
            raise TypeError("argument 'value' must be \
                of type 'int' or 'float'")


        # ensure validity of 'alpha' in options
        elif('alpha' not in options):
            raise TypeError("required argument 'alpha' \
                not specified")
        elif(not isinstance(options['alpha'], int) and 
            not isinstance(options['alpha'], float)):
            raise TypeError("argument 'alpha' must be \
                of type 'int' or 'float'")
        elif(options['alpha'] < 0 or options['alpha'] > 1):
            raise ValueError("argument 'alpha' must be \
                between 0-1 inclusively")


        # ensure validity of 'rgb' in options
        elif('rgb' not in options):
            raise TypeError("required argument 'rgb' not \
                specified")
        elif(not isinstance(options['rgb'], str)):
            raise TypeError("argument 'rgb' must be of type 'str'")

        elif(not Themes().is_rgb_hex(options['rgb'])):
            raise ValueError("argument 'rgb' must be \
                between #000000 to \
                #ffffff, and preceded with '#'")



        # ensure validity of 'label' in options if it is ever passed.
        elif('label' not in options):
            self.__label = None
        elif('label' in options):
            if(not isinstance(options['label'], str) and options['label'] is not None):
                raise TypeError("argument 'label' must be of type 'str'")
            self.__label = options['label']




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


    @property
    def label(self):
        ''' get laebel '''
        return self.__label



    # @alpha.setter
    # def alpha(self, value):
    #     ''' set the alpha value '''
    #     self.__alpha = value

    # @rgb.setter
    # def rgb(self, value):
    #     ''' set the rgb color code '''
    #     self.__rgb = value



    # @label.setter
    # def label(self, value):
    #     ''' set the label '''
    #     self.__label = value


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
            raise TypeError("required argument 'data' \
                not specified")
        elif(not isinstance(options['data'],list)):
            raise TypeError("argument 'data' must be of type \
                'list', i.e. list of lists")
        for row in options['data']:
            if(not isinstance(row, list)):
                raise TypeError("argument 'data' must be of type \
                    'list', i.e. list of lists")

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
        if(not isinstance(row, int)):
            raise TypeError("required arguments 'row' and 'col' must be of type 'int'")
        elif(not isinstance(col, int)):
            raise TypeError("required arguments 'row' and 'col' must be of type 'int'")


        try:
            item = self.__grid[row][col]
            return item
        except IndexError:
            raise IndexError("required arguments 'row' or 'col' is out of range.")
        except Exception:
            raise Exception("An unknown error occured")


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



    def get_min_value(self):
        ''' get minimum value in the whole grid '''
        grid = self.__grid
        min_values = list()
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

        # determine the minimum value in this
        # DataGrid object.
        for row in range(firstRow, len(grid)):
            row_min = list()
            for col in range(firstCol, len(grid[0])):
                try:
                    row_min.append(grid[row][col])
                except:
                    continue
            if(len(row_min)!=0):
                min_values.append(min(row_min))
        # return the minimum value.
        return min(min_values)




    
    
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
            raise TypeError("argument 'data' must be of type 'list' \
                (i.e. list of lists) and further contain items of \
                type 'str' or 'Tile'")
        for row in options['data']:
            if(not isinstance(row, list)):
                raise TypeError("argument 'data' must be of type \
                    'list' (i.e. list of lists) and further contain \
                    items of type 'str' or 'Tile'")
            else:
                for field in row:
                    if(not isinstance(field, str) and 
                        not isinstance(field, Tile)):
                        raise TypeError("argument 'data' must be of \
                            type 'list' (i.e. list of lists) and further \
                            contain items of type 'str' or 'Tile'")
        

        if('title' not in options):
            raise TypeError("required argument 'title' \
                not specified")
        elif(not isinstance(options['title'], str)):
            raise TypeError("argument 'title' must be of \
                type 'str'")
        elif('subtitle' not in options):
            raise TypeError("required argument 'subtitle' \
                not specified")
        elif(not isinstance(options['subtitle'], str)):
            raise TypeError("argument 'subtitle' must be \
                of type 'str'")
        elif('theme' not in options):
            raise TypeError("required argument 'theme' \
                not specified")
        elif(not isinstance(options['theme'], Theme)):
            raise TypeError("argument 'theme' must be of \
                type 'Theme'")
        elif('stylesheet' not in options):
            raise TypeError("required argument 'stylesheet' \
                not specified")
        elif(not isinstance(options['stylesheet'], StyleSheet)):
            raise TypeError("argument 'stylesheet' must be \
                of type 'StyleSheet'")
        elif('xaxis_title' not in options):
            raise TypeError("required argument 'xaxis_title' \
                not specified")
        elif(not isinstance(options['xaxis_title'], str)):
            raise TypeError("argument 'xaxis_title' must be \
                of type 'str'")
        elif('yaxis_title' not in options):
            raise TypeError("required argument 'yaxis_title' \
                not specified")
        elif(not isinstance(options['yaxis_title'], str)):
            raise TypeError("argument 'yaxis_title' must be \
                of type 'str'")


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
        if('data_formatter' in options):
            self.__data_formatter = options['data_formatter']
        else:
            self.__data_formatter = None
        if('grouping' in options):
            if(options['grouping'] is not None):
                if(not isinstance(options['grouping'], TileGroups)):
                    raise TypeError("argument 'grouping' must be of type 'TileGroup'")
                else:
                    self.__grouping = options['grouping']
            else:
                self.__grouping = None
        else:
            self.__grouping = None


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


    @property
    def dataformatter(self):
        ''' get data formatter if exists '''
        return self.__data_formatter



    @property
    def grouping(self):
        ''' get TileGroup object for heatmap if exists '''
        return self.__grouping


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















class TileGroup:

    def __init__(self, left, right, inclusive_left=True, 
        inclusive_right=False, label="", color=None):

        # define class variables.
        self.left = left
        self.right = right
        self.inclusive_left = inclusive_left
        self.inclusive_right = inclusive_right
        self.label = label
        self.color = color

        # validate all arguments.
        self.__validate()

        # convert color to hex where necessary.
        if(Themes().is_rgb_hex(self.color)):
            self.color = color
        elif(Themes().is_color_name(self.color)):
            self.color = Themes().colors[self.color]
        

    def __validate(self):

        # left must ONLY be int, float or None
        if(not isinstance(self.left, int)
           and not isinstance(self.left, float)
           and self.left is not None):
            raise TypeError("arguments 'left' and 'right' can only be of type 'int', 'float', or None")
            
        # right must ONLY be int, float or None
        if(not isinstance(self.right, int)
           and not isinstance(self.right, float)
           and self.right is not None):
            raise TypeError("arguments 'left' and 'right' can only be of type 'int', 'float', or None")
        
        # left value should be less than right value.
        if((isinstance(self.left,float) or isinstance(self.left, int)) and
           (isinstance(self.right,int) or isinstance(self.right,float))):            
            if(self.left > self.right):
                raise ValueError("argument 'left' must be less than 'right'")

        # left and right cannot BOTH be false.
        if(self.left == False and self.right == False):
            raise ValueError("only one out of arguments 'left' and 'right can be 'False'")

        # inclusive left must only be bool
        if(not isinstance(self.inclusive_left, bool)):
            raise TypeError("argument 'inclusive_left' must be of type 'bool'")

        # inclusive right must only be bool
        if(not isinstance(self.inclusive_right, bool)):
            raise TypeError("argument 'inclusive_right' must be of type 'bool'")

        # label must be specified
        if(self.label == ""):
            raise TypeError("required argument 'label' must be specified, and must be of type 'str'")

        # label must only be string.
        if(not isinstance(self.label, str)):
            raise TypeError("argument 'label' must be of type 'str'")

        # color, if specified, must be a valid hex, or color string
        if(self.color is not None):
            if(not Themes().is_rgb_hex(self.color) and not Themes().is_color_name(self.color)):
                raise TypeError("argument 'color' must be color hex string, or valid color name")


    def __str__(self):
        left = self.left
        right = self.right
        label = self.label
        if(not left):
            left = "-"
        if(not right):
            right = "+"
        return "{} = ({},{})".format(label,left, right)


    def __repr__(self):
        left = self.left
        right = self.right
        label = self.label
        if(not left):
            left = "-"
        if(not right):
            right = "+"
        return "{} = ({},{})".format(label,left, right)
    
        
    def in_group(self, data):

        # validation of argument 'data'
        if(not isinstance(data, int) and not isinstance(data,float)):
            raise TypeError("required argument 'data' must be of type 'int' or 'float'")

        inc_right = self.inclusive_right
        inc_left = self.inclusive_left
        if(not self.left and self.right):
            # means we dealing with low to infinity bound
            if(inc_right):
                if(data <= self.right):
                    return True
                else:
                    return False
            elif(not inc_right):
                if(data < self.right):
                    return True
                else:
                    return False
            else:
                # do nothing if no inclusivity specified.
                pass

        elif(not self.right and self.left):
            # means we dealing with a right to infinity bound
            if(inc_right):
                if(data >= self.left):
                    return True
                else:
                    return False
            elif(not inc_right):
                if(data > self.left):
                    return True
                else:
                    return False
            else:
                # do nothing if no inclusivity specified.
                pass

        elif(self.left and self.right):
            # means we have a left and right bound
            l = self.left
            r = self.right

            if(inc_left == True and inc_right == True):
                if(data >= self.left and data <= self.right):
                    return True
                else:
                    return False
            elif(inc_left == True and inc_right == False):
                if(data >= self.left and data < self.right):
                    return True
                else:
                    return False
            elif(inc_left == False and inc_right == True):
                if(data > self.left and data <= self.right):
                    return True
                else:
                    return False
            elif(inc_left == False and inc_right == False):
                if(data > self.left and data < self.right):
                    return True
                else:
                    return False
        else:
            raise Exception("Unknown error occured")













class TileGroups:

    def __init__(self, *groups):
        self.groups = groups
        self.__validate()


    def __validate(self):
        for group in self.groups:
            if(not isinstance(group, TileGroup)):
                raise TypeError("all tile groups passed must be of type 'TileGroup'")

    def __is_numeric(self, value):
        if(isinstance(value, int) or isinstance(value, float)):
            return True
        else:
            return False

    def __is_none(self, value):
        if(value == None):
            return True
        else:
            return False




    def alpha(self, value):
        group = self.group(value)
        if(group is None):
            return 0.0
        else:
            index = self.groups.index(group)
            index += 1
            alpha = (1/len(self.groups))*(index)
            return alpha




    def group(self, value):
        if(not isinstance(value, int) and
           not isinstance(value, float)):
            raise TypeError("required argument 'value' must be of type 'int' or 'float'")
        
        for group in self.groups:

            # if both left, right are numeric
            if(self.__is_numeric(group.left) and self.__is_numeric(group.right)):                
                l = 0
                r = 0
                if(group.inclusive_left):
                    l = group.left
                else:
                    l = group.left + 1
                if(group.inclusive_right):
                    r = group.right + 1
                else:
                    r = group.right

                if(value >= l and value <= r):
                    return group

            # if left None, right numeric
            if(group.left == None and self.__is_numeric(group.right)):                
                r = group.right
                if(group.inclusive_right):
                    if(value <= r):
                        return group

                else:
                    if(value < r):
                        return group

            # if left numeric, right None
            if(self.__is_numeric(group.left) and group.right == None):                
                l = group.left
                if(group.inclusive_left):
                    if(value >= l):
                        return group

                else:
                    if(value > l):
                        return group
        return None

    


    def label(self, value):
        group = self.group(value)
        if(group is None):
            return None
        else:
            return group.label
    


    def __str__(self):
        str_rep = "TileGroups("
        for i in range(len(self.groups)):
            if(i == (len(self.groups)-1)):
                #str_rep += self.groups[i].label+" = "
                str_rep += str(self.groups[i])
            else:
                #str_rep += self.groups[i].label+" = "
                str_rep += str(self.groups[i])+", "
        str_rep += ")"
        return str_rep




        


    def __repr__(self):
        str_rep = "TileGroups("
        for i in range(len(self.groups)):
            if(i == (len(self.groups)-1)):
                #str_rep += self.groups[i].label+" = "
                str_rep += str(self.groups[i])
            else:
                #str_rep += self.groups[i].label+" = "
                str_rep += str(self.groups[i])+", "
        str_rep += ")"
        return str_rep

