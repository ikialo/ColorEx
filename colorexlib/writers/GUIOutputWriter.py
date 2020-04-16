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

from .OutputWriter import OutputWriter
from .HeatMapWindow import HeatMapWindow
from tkinter import *

class GUIOutputWriter(OutputWriter):
        

        ''' Class facilitates writing of heat 
        maps and grids to the screen GUI '''

        def __init__(self,heatmap=None,stylesheet=None):
                ''' Initialize GUIOutputWriter object '''
                self.heatmap = heatmap
                self.stylesheet = stylesheet
                


        def write(self):
                ''' outputs the heat map to the screen GUI '''
                root = Tk()
                root.title("Heat Map in ColorEx")
                f = HeatMapWindow(root, heatmap=self.heatmap,
                                  stylesheet=self.stylesheet)
                root.mainloop()

                

        def write2(self):
                ''' outputs the heat map to the screen GUI '''
                root = Tk()
                root.title("Heat Map in ColorEx")
                f = HeatMapWindow(root, heatmap=self.heatmap)
                root.mainloop()
