# import modules 
from colorexlib.colorex import ColorExGrid

# set tile grid options
options = dict()
options['source'] = ['data\\the_weather.csv', 'csv']
options['title'] = 'Weather Data 2017'
options['subtitle'] = 'The general weather data for year 2017'
options['theme'] = 'themes\\barbie.cxt'

# create ColorEx object, passing options.
colorex_grid = ColorExGrid(options)

# create color grid in HTML
colorex_grid.to_html('the_weather.html',
    'templates\\default.html')
