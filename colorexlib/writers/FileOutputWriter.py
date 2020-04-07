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

from abc import ABC, abstractmethod, abstractproperty
from .OutputWriter import OutputWriter

class FileOutputWriter(OutputWriter):

    ''' Class represents all output file writers '''

    def __init__(self, filepath, heat_map):
        ''' Initialize FileOutputWriter object '''
        self.__filepath = filepath
        self.__heat_map = heat_map

    @property
    def filepath(self):
        ''' get file path '''
        filepath = self.__filepath
        return filepath

    @property
    def heat_map(self):
        ''' get the heat map (list of lists) '''
        heatmap = self.__heat_map
        return heatmap
    
    def write(self, options):
        ''' write heat map to output file '''
        pass
