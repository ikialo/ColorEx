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


from ..common.datastructures import Data, DataGrid
import csv
from .FileInputReader import FileInputReader

class CSVReader(FileInputReader):

    ''' CSV data reader for a CSV data file '''

    def __init__(self, filepath, rowcol_headers=True):
        ''' Initialize CSVReader object '''

        # call the parent class initializer
        FileInputReader.__init__(self, filepath)


        if(not isinstance(rowcol_headers, bool)):
            raise TypeError("argument 'rowcol_headers' \
                must be of type 'bool'")


        #self.__filepath = filepath
        #self.__data = list()
        self.__rowcolheaders = rowcol_headers
        self.read()




    @property
    def rowcolheaders(self):
        ''' is the first row of data skipped '''
        return self.__rowcolheaders




    def read(self):
        ''' read the CSV file '''
        filepath = self.filepath
        tempdata = list()
        rowcount = 0
        # read csv and convert each row to float 
        # where necessary.
        with open(filepath) as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            for row in reader:
                if(self.rowcolheaders and rowcount == 0):
                    new_row = row
                elif(self.rowcolheaders and rowcount != 0):
                    new_row = self.row_to_float(row, 
                        self.rowcolheaders)
                else:
                    new_row = self.row_to_float(row, 
                        self.rowcolheaders)
                rowcount += 1
                tempdata.append(new_row)
        # set class object data to the read csv data.
        self.data = tempdata




    def row_to_float(self, row, rowcolheaders):
        ''' convert numeric data in row to float data type '''
        r = list()
        if(rowcolheaders):
            row_header = row[0]
            row = row[1:]
        for item in row:
            try:
                data_item = float(item)
                r.append(data_item)
            except:
                r.append(item)
        if(rowcolheaders):
            r.insert(0,row_header)
        return r





    def generate_datagrid(self):
        ''' generate a DataGrid object based on 
        CSV file data '''
        data = self.data
        new_data = list()
        # convert all 'float' values to
        # Data items.
        for row in data:
            new_row = list()
            for item in row:
                if(type(item) is float):
                    new_row.append(Data(item))
                else:
                    new_row.append(item)
            new_data.append(new_row)
        # create a DataGrid object, passing options.
        data_grid = DataGrid({"data": new_data, 
            'rowcol_headers': self.rowcolheaders})
        return data_grid
        






