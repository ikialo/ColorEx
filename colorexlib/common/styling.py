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
import math
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
        ''' returns dictionary of in-built themes '''
        return self.__themes


    @property
    def colors(self):
        ''' returns list of in-built colors '''
        return self.__colors



    def is_rgb_hex(self, hex_code):
        ''' confirms whether or not a RGB hex code is valid '''
        if(not isinstance(hex_code, str)):
            return False
        if(hex_code[0] == '#' and len(hex_code) == 7):
            try:
                int(hex_code[1:],16)
                return True
            except:
                return False
        else:
            return False


    def is_rgb_decimal(self, decimal):
        ''' confirms whether or not a RGB decimal code is valid '''
        if(not isinstance(decimal, tuple)):
            return False
        elif(not isinstance(decimal[0],int) or 
            not isinstance(decimal[1],int) or 
            not isinstance(decimal[2],int)):
            return False
        elif(decimal[0] not in range(0,256) or decimal[1] 
            not in range(0,256) or decimal[2] not in range(0,256)):
            return False
        else:
            return True





    def rgb_hex_to_decimal(self, rgb_hex):
        ''' converts rgb hex color code to decimal (0-255) '''
        if(not self.is_rgb_hex(rgb_hex)):
            raise TypeError("argument 'rgb_hex' must be a valid \
                hex, type 'str' between #000000 to #ffffff.")
        else:
            rgb_hex = rgb_hex[1:]
        try:
            r = int(re.findall('..', str(rgb_hex))[0], base=16)
            g = int(re.findall('..', str(rgb_hex))[1], base=16)
            b = int(re.findall('..', str(rgb_hex))[2], base=16)
            return (r,g,b)
        except:
            raise TypeError("argument 'rgb_hex' must be a valid \
                hex, type 'str' between #000000 to #ffffff.")






    def decimal_to_rgb_hex(self, decimal):
        ''' converts decimal code color to rgb hex code '''

        if(not self.is_rgb_decimal(decimal)):
            raise TypeError("argument 'decimal' must be of \
                type tuple between (0,0,0) to (255,255,255)")

        r = hex(decimal[0]).replace('0x','')
        g = hex(decimal[1]).replace('0x','')
        b = hex(decimal[2]).replace('0x','')
        if(len(r)==1):
            r = '0'+r
        if(len(g)==1):
            g = '0'+g
        if(len(b)==1):
            b = '0'+b
        return '#'+r+g+b




    # def generate_alpha_rgbcolor(self, rgb, alpha):
    #     ''' Generates color between passed rgb decimal 
    #     color and white, based on alpha '''

    #     if(not self.is_rgb_decimal(rgb)):
    #         raise TypeError("argument 'rgb' must be of type \
    #             tuple between (0,0,0) to (255,255,255)")

    #     elif(not isinstance(alpha, float)):
    #         raise TypeError("argument 'alpha' must be of type \
    #             float, between 0-1 inclusively")

    #     elif(alpha < 0 or alpha > 1):
    #         raise TypeError("argument 'alpha' must be of type \
    #             float, between 0-1 inclusively")            

    #     r = rgb[0]
    #     g = rgb[1]
    #     b = rgb[2]
    #     n_colors = max(r,g,b)
    #     increment = int(alpha*n_colors)
    #     r += increment
    #     g += increment
    #     b += increment
    #     if(r>255):
    #         r = 255
    #     if(g>255):
    #         g = 255
    #     if(b>255):
    #         b = 255

    #     return (r,g,b)




    def generate_alpha_rgb_bicolor(self, rgb1, rgb2, alpha):
        ''' Generates color between 2 rgb decimal colors, 
        based on alpha '''
        

        if(not self.is_rgb_decimal(rgb1)):
            raise TypeError("argument 'rgb1' must be of type \
                tuple between (0,0,0) to (255,255,255)")

        if(not self.is_rgb_decimal(rgb2)):
            raise TypeError("argument 'rgb2' must be of type \
                tuple between (0,0,0) to (255,255,255)")


        elif(not isinstance(alpha, float)):
            raise TypeError("argument 'alpha' must be of type \
                float, between 0-1 inclusively")

        elif(alpha < 0 or alpha > 1):
            raise TypeError("argument 'alpha' must be of type \
                float, between 0-1 inclusively")            

        ramount = math.trunc((rgb1[0] - rgb2[0])*alpha)
        gamount = math.trunc((rgb1[1] - rgb2[1])*alpha)
        bamount = math.trunc((rgb1[2] - rgb2[2])*alpha)
        r_new = rgb2[0] + (ramount)
        g_new = rgb2[1] + (gamount)
        b_new = rgb2[2] + (bamount)
        return (r_new,g_new,b_new)



    

    def is_color_name(self, color_name):
        ''' confirms whether or not a color name is 
        valid, based on internal color dictionary '''
        if(color_name in self.__colors.keys()):
            return True
        else:
            return False   

















class Theme:

    def __init__(self, primaryColor="#000000",
        secondaryColor="#ffffff", onPrimaryColor="#ffffff",
        onSecondaryColor="#000000", backgroundColor="#ffffff",
        onBackgroundColor="#000000"):



        # ensure all arguments passed are valid.
        if(not Themes().is_rgb_hex(primaryColor) 
            and primaryColor not in Themes().colors):
            raise TypeError("argument 'primaryColor' \
                must be a valid hex, type 'str' between \
                #000000 to #ffffff, or a supported color name.")

        elif(not Themes().is_rgb_hex(secondaryColor) 
            and secondaryColor not in Themes().colors):
            raise TypeError("argument 'secondaryColor' \
                must be a valid hex, type 'str' between \
                #000000 to #ffffff, or a supported color name.")

        elif(not Themes().is_rgb_hex(onPrimaryColor) 
            and onPrimaryColor not in Themes().colors):
            raise TypeError("argument 'onPrimaryColor' \
                must be a valid hex, type 'str' between \
                #000000 to #ffffff, or a supported color name.")

        elif(not Themes().is_rgb_hex(onSecondaryColor) 
            and onSecondaryColor not in Themes().colors):
            raise TypeError("argument 'onSecondaryColor' \
                must be a valid hex, type 'str' between \
                #000000 to #ffffff, or a supported color name.")

        elif(not Themes().is_rgb_hex(onBackgroundColor) 
            and onBackgroundColor not in Themes().colors):
            raise TypeError("argument 'onBackgroundColor' \
                must be a valid hex, type 'str' between \
                #000000 to #ffffff, or a supported color name.")


        # prepare color palette
        self.__palette = dict()
        self.__palette['primary'] = primaryColor
        self.__palette['secondary'] = secondaryColor
        self.__palette['on-primary'] = onPrimaryColor
        self.__palette['on-secondary'] = onSecondaryColor
        self.__palette['background'] = backgroundColor
        self.__palette['on-background'] = onBackgroundColor

        # do conversion of the colors from color names 
        # to color codes if necessary
        if(Themes().is_color_name(primaryColor)):
            self.__palette['primary'] = Themes().\
            colors[primaryColor]
        if(Themes().is_color_name(secondaryColor)):
            self.__palette['secondary'] = Themes().\
            colors[secondaryColor]
        if(Themes().is_color_name(onPrimaryColor)):
            self.__palette['on-primary'] = Themes().\
            colors[onPrimaryColor]
        if(Themes().is_color_name(onSecondaryColor)):
            self.__palette['on-secondary'] = Themes().\
            colors[onSecondaryColor]
        if(Themes().is_color_name(backgroundColor)):
            self.__palette['background'] = Themes().\
            colors[backgroundColor]
        if(Themes().is_color_name(onBackgroundColor)):
            self.__palette['on-background'] = Themes().\
            colors[onBackgroundColor]


    @property
    def palette(self):
        ''' returns a dictionary color 
        palette for the current theme '''
        return self.__palette










class StyleSheet:

    def __init__(self, tile_size=(60,60), plane_top_margin=117, 
                 canvas_size_factor=0.9, canvas_top_margin=20,
                 canvas_bottom_margin=20, ylabel_margin=10,
                 xlabel_margin=2, axes_title_font="Arial", 
                 axes_title_size=14, axes_title_bold=True,
                 axes_tick_length=10, axes_label_font="Arial", 
                 axes_label_size=10, axes_label_bold=False, 
                 title_font="Arial", title_size=22, title_bold=False,
                 title_ycoord=30, subtitle_font="Arial", 
                 subtitle_size=13, subtitle_bold=False, 
                 subtitle_ycoord=70):


        # ensure all arguments passed are valid
        if(not isinstance(tile_size, tuple)):
            raise TypeError("argument 'tile_size' must be \
                of type tuple, and of form (width, height) \
                where 'width' and 'height' are of type 'int'")
        elif(len(tile_size) != 2):
            raise TypeError("argument 'tile_size' must be \
                of type tuple, and of form (width, height) \
                where 'width' and 'height' are of type 'int'")
        elif(not isinstance(tile_size[0], int) or 
            not isinstance(tile_size[1], int)):
            raise TypeError("argument 'tile_size' must be of \
                type tuple, and of form (width, height) where \
                'width' and 'height' are of type 'int'")

        elif(not isinstance(plane_top_margin, int)):
            raise TypeError("argument 'plane_top_margin' must \
                be of type 'int'")
        elif(not isinstance(canvas_size_factor, float)):
            raise TypeError("argument 'canvas_size_factor' must \
                be of type 'float, between 0-1'")
        elif(canvas_size_factor < 0 or canvas_size_factor > 1):
            raise TypeError("argument 'canvas_size_factor' must \
                be of type 'float, between 0-1'")
        elif(not isinstance(canvas_top_margin, int)):
            raise TypeError("argument 'canvas_top_margin' must \
                be of type 'int'")
        elif(not isinstance(canvas_bottom_margin, int)):
            raise TypeError("argument 'canvas_bottom_margin' must \
                be of type 'int'")
        elif(not isinstance(ylabel_margin, int)):
            raise TypeError("argument 'ylabel_margin' must \
                be of type 'int'")
        elif(not isinstance(xlabel_margin, int)):
            raise TypeError("argument 'xlabel_margin' must be \
                of type 'int'")
        elif(not isinstance(axes_title_font, str)):
            raise TypeError("argument 'axes_title_font' must \
                be of type 'str'")
        elif(not isinstance(axes_title_size, int)):
            raise TypeError("argument 'axes_title_size' must \
                be of type 'int'")
        elif(not isinstance(axes_title_bold, bool)):
            raise TypeError("argument 'axes_title_bold' must \
                be of type 'bool'")
        elif(not isinstance(axes_tick_length, int)):
            raise TypeError("argument 'axes_tick_length' must \
                be of type 'int'")
        elif(not isinstance(axes_label_font, str)):
            raise TypeError("argument 'axes_label_font' must \
                be of type 'str'")
        elif(not isinstance(axes_label_size, int)):
            raise TypeError("argument 'axes_label_size' must \
                be of type 'int'")
        elif(not isinstance(axes_label_bold, bool)):
            raise TypeError("argument 'axes_label_bold' must \
                be of type 'bool'")
        elif(not isinstance(title_font, str)):
            raise TypeError("argument 'title_font' must be of \
                type 'str'")
        elif(not isinstance(title_size, int)):
            raise TypeError("argument 'title_size' must be of \
                type 'int'")
        elif(not isinstance(title_bold, bool)):
            raise TypeError("argument 'title_bold' must be of \
                type 'bool'")
        elif(not isinstance(title_ycoord, int)):
            raise TypeError("argument 'title_ycoord' must be \
                of type 'int'")
        elif(not isinstance(subtitle_font, str)):
            raise TypeError("argument 'subtitle_font' must be \
                of type 'str'")
        elif(not isinstance(subtitle_size, int)):
            raise TypeError("argument 'subtitle_size' must be \
                of type 'int'")
        elif(not isinstance(subtitle_bold, bool)):
            raise TypeError("argument 'subtitle_bold' must be \
                of type 'bool'")
        elif(not isinstance(subtitle_ycoord, int)):
            raise TypeError("argument 'subtitle_ycoord' must \
                be of type 'int'")

        # prepare and set all the styles
        self.__styles = dict()
        self.__styles['tile_size'] = tile_size
        # plane settings
        self.__styles['plane_top_margin'] = plane_top_margin

        # canvas settings
        self.__styles['canvas_size_factor'] = canvas_size_factor 
        self.__styles['canvas_top_margin'] = canvas_top_margin
        self.__styles['canvas_bottom_margin'] = canvas_bottom_margin

        # axes label margin settings
        self.__styles['ylabel_margin'] = ylabel_margin
        self.__styles['xlabel_margin'] = xlabel_margin

        # axes title settings.
        self.__styles['axes_title_font'] = axes_title_font
        self.__styles['axes_title_size'] = axes_title_size
        self.__styles['axes_title_bold'] = axes_title_bold
        self.__styles['axes_tick_length'] = axes_tick_length
        self.__styles['axes_label_font'] = axes_label_font
        self.__styles['axes_label_size'] = axes_label_size
        self.__styles['axes_label_bold'] = axes_label_bold

        # title settings.
        self.__styles['title_font'] = title_font
        self.__styles['title_size'] = title_size
        self.__styles['title_bold'] = title_bold
        self.__styles['title_ycoord'] = title_ycoord

        # subtitle settings.
        self.__styles['subtitle_font'] = subtitle_font
        self.__styles['subtitle_size'] = subtitle_size
        self.__styles['subtitle_bold'] = subtitle_bold
        self.__styles['subtitle_ycoord'] = subtitle_ycoord


    @property
    def styles(self):
        ''' returns a dictionary styles for 
        the current stylesheets '''
        return self.__styles



