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



class DataFormatter:

    def __init__(self, prefix="", suffix="",
                 format_strings=list()):

        # ensure validity of parameters
        if(not isinstance(format_strings, list)):
            raise TypeError("argument 'format_strings' must \
                be of type 'list'")
        else:
            for item in format_strings:
                if(not isinstance(item, str)):
                    raise TypeError("argument 'format_strings' \
                        must be of type list, and contain \
                        elements of type 'str'")
        
        self.prefix = str(prefix)
        self.suffix = str(suffix)
        self.formats = format_strings
        


    def format(self, data):
        final_data = str(data)
        if(len(self.formats)!=0):
            for format_str in self.formats:
                final_data = format(data, format_str)
            return self.prefix+str(final_data)+self.suffix
        else:
            return data