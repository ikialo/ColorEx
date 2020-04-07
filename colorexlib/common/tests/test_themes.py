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

from ..themes import Theme, Themes
import pytest


''' Themes class tests '''

def test_Themes_themes():
    themes = Themes()
    assert themes.themes == {'default': {'primary': '#0044aa', 'secondary': '#aaccff', 'on-primary': '#d7eef4', 'on-secondary': '#f9f9f9'}, 'sun': {'primary': '#d45500', 'secondary': '#ffccaa', 'on-primary': '#ffccaa', 'on-secondary': '#000000'}}




def test_Themes_colors():
    themes = Themes()
    colors = themes.colors
    assert type(colors) == type(dict())

    assert colors['default'] == '#000000'
    assert colors['black'] == '#000000'
    assert colors['white'] == '#ffffff'
    assert colors['red'] == '#ff0000'
    assert colors['lime'] == '#00ff00'
    assert colors['blue'] == '#0000ff'
    assert colors['yellow'] == '#ffff00'
    assert colors['cyan'] == '#00ffff'
    assert colors['aqua'] == '#00ffff'
    assert colors['magenta'] == '#ff00ff'
    assert colors['fuchsia'] == '#ff00ff'
    assert colors['silver'] == '#c0c0c0'
    assert colors['gray'] == '#808080'
    assert colors['grey'] == '#808080'
    assert colors['maroon'] == '#800000'
    assert colors['olive'] == '#808000'
    assert colors['green'] == '#008000'
    assert colors['purple'] == '#800080'
    assert colors['teal'] == '#008080'
    assert colors['navy'] == '#000080'



def test_Themes_is_rgb_hex():
	themes = Themes()
	assert themes.is_rgb_hex('#ff0011') == True
	assert themes.is_rgb_hex('ff0022') == False
	assert themes.is_rgb_hex('#ff9*&^') == False
	assert themes.is_rgb_hex('#88aabb00') == False
	assert themes.is_rgb_hex('#00aakk') == False
	assert themes.is_rgb_hex('#00aaff') == True




def test_CX_HeatMap_rgb_hex_to_decimal():
    themes = Themes()
    assert themes.rgb_hex_to_decimal('#ff0000') == (255,0,0)
    assert themes.rgb_hex_to_decimal('#000000') == (0,0,0)
    assert themes.rgb_hex_to_decimal('#00ff00') == (0,255,0)
    assert themes.rgb_hex_to_decimal('#00ff00') == (0,255,0)
    assert themes.rgb_hex_to_decimal('#00ffzz') == False
    assert themes.rgb_hex_to_decimal('22aa00') == False





def test_CX_HeatMap_is_color_name():
    themes = Themes()
    assert themes.is_color_name('blue') == True
    assert themes.is_color_name('redigo') == False
    assert themes.is_color_name('red') == True
    assert themes.is_color_name('yellowish') == False
    assert themes.is_color_name('pink') == False






''' Theme class tests '''
def test_Theme_palette():
    theme1 = Theme()
    assert theme1.palette == {'primary': '#0044aa', 'secondary': '#aaccff', 'on-primary': '#d7eef4', 'on-secondary': '#f9f9f9'}
    theme2 = Theme(name='sun')
    assert theme2.palette == {'primary': '#d45500', 'secondary': '#ffccaa', 'on-primary': '#ffccaa', 'on-secondary': '#000000'}




