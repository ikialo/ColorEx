# import modules 
from colorexlib.colorex import ColorExGrid

# set tile grid options
options = dict()
options['source'] = ['data\\website_traffic.csv', 'csv']
options['title'] = 'Website Traffic 2017'
options['subtitle'] = 'The website traffic for whatever.com in 2017'
options['theme'] = 'default'

# create ColorEx object, passing options.
colorex_grid = ColorExGrid(options)

# create color grid in HTML
colorex_grid.to_html('website_traffic.html',
    'templates\\template.html')
