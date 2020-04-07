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

import xml.etree.ElementTree as ET
import re


class Themes:

    def __init__(self):
        # general theme repo.
        self.__themes = dict()

        # general colors repo.
        self.__colors = dict()


        # declare default theme.
        default = dict()
        default['primary'] = '#0044aa'
        default['secondary'] = '#aaccff'
        default['on-primary'] = '#d7eef4'
        default['on-secondary'] = '#f9f9f9'


        # declare sun theme
        sun = dict()
        sun['primary'] = '#d45500'
        sun['secondary'] = '#ffccaa'
        sun['on-primary'] = '#ffccaa'
        sun['on-secondary'] = '#000000'

    
        # add all declared themes to the repo.
        self.__themes['default'] = default
        self.__themes['sun'] = sun


        # declare rgb color codes, and their names.
        self.__colors['default'] = '#000000'
        self.__colors['black'] = '#000000'
        self.__colors['white'] = '#ffffff'
        self.__colors['red'] = '#ff0000'
        self.__colors['lime'] = '#00ff00'
        self.__colors['blue'] = '#0000ff'
        self.__colors['yellow'] = '#ffff00'
        self.__colors['cyan'] = '#00ffff'
        self.__colors['aqua'] = '#00ffff'
        self.__colors['magenta'] = '#ff00ff'
        self.__colors['fuchsia'] = '#ff00ff'
        self.__colors['silver'] = '#c0c0c0'
        self.__colors['gray'] = '#808080'
        self.__colors['grey'] = '#808080'
        self.__colors['maroon'] = '#800000'
        self.__colors['olive'] = '#808000'
        self.__colors['green'] = '#008000'
        self.__colors['purple'] = '#800080'
        self.__colors['teal'] = '#008080'
        self.__colors['navy'] = '#000080'




    @property
    def themes(self):
        ''' returns list of in-built themes '''
        return self.__themes


    @property
    def colors(self):
        ''' returns list of in-built colors '''
        return self.__colors



    def is_rgb_hex(self, hex_code):
        ''' confirms whether or not a RGB hex code is valid '''
        if(hex_code[0] == '#' and len(hex_code) == 7):
            try:
                int(hex_code[1:],16)
                return True
            except:
                return False
        else:
            return False




    def rgb_hex_to_decimal(self, rgb_hex):
        if(rgb_hex[0]=='#'):
            rgb_hex = rgb_hex[1:]
        else:
            return False
        try:
            r = int(re.findall('..', str(rgb_hex))[0], base=16)
            g = int(re.findall('..', str(rgb_hex))[1], base=16)
            b = int(re.findall('..', str(rgb_hex))[2], base=16)
            return (r,g,b)
        except:
            return False



    def is_color_name(self, color_name):
        ''' confirms whether or not a color name is valid, based
        on internal color dictionary '''
        if(color_name in self.__colors.keys()):
            return True
        else:
            return False   







class Theme:

    def __init__(self, filename=None, name='default'):


        # prepare color palette
        self.__palette = dict()
        self.__palette['primary'] = ''
        self.__palette['secondary'] = ''
        self.__palette['on-primary'] = ''
        self.__palette['on-secondary'] = ''



        # validation of parameters
        if(filename == None and name=='default'):
            # go with default settings.
            all_themes = Themes()
            the_theme = all_themes.themes['default']
            self.__palette['primary'] = the_theme['primary']
            self.__palette['secondary'] = the_theme['secondary']
            self.__palette['on-primary'] = the_theme['on-primary']
            self.__palette['on-secondary'] = the_theme['on-secondary']

        elif(filename == None and name != 'default'):
            # go with theme name specified, using in-built theme.
            try:
                all_themes = Themes()
                the_theme = all_themes.themes[name]
                self.__palette['primary'] = the_theme['primary']
                self.__palette['secondary'] = the_theme['secondary']
                self.__palette['on-primary'] = the_theme['on-primary']
                self.__palette['on-secondary'] = the_theme['on-secondary']
            except:
                raise Exception
                        

        elif((filename != None and name == 'default') or (filename != None and name != 'default')):
            # go with the theme declared in the theme file specified.
            # read theme from theme file (XML-formatted .cxt file)
            try:
                tree = ET.parse(filename)
                root = tree.getroot()
                # extract theme data from .cxt XML file
                all_theme_colors = list(root)
                for color in all_theme_colors:
                    if(color.get('name') == 'primary'):
                        self.__palette['primary'] = color.get('value')
                        
                    elif(color.get('name') == 'secondary'):
                        self.__palette['secondary'] = color.get('value')
                        
                    elif(color.get('name') == 'on-primary'):
                        self.__palette['on-primary'] = color.get('value')
                        
                    elif(color.get('name') == 'on-secondary'):
                        self.__palette['on-secondary'] = color.get('value')

                    else:
                        continue

            except:
                raise Exception
        

        else:
            # just go with the default.
            # go with default settings.
            all_themes = Themes()
            the_theme = all_themes.themes['default']
            self.__palette['primary'] = the_theme['primary']
            self.__palette['secondary'] = the_theme['secondary']
            self.__palette['on-primary'] = the_theme['on-primary']
            self.__palette['on-secondary'] = the_theme['on-secondary']        
        




    @property
    def palette(self):
        ''' returns a dictionary color palette for the current theme '''
        return self.__palette
