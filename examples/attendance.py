# import modules 
from colorex.colorex import ColorExGrid

# set tile grid options
options = dict()
options['source'] = ['data\\attendance.csv', 'csv']
options['title'] = 'Student Attendance'
options['subtitle'] = 'Attendance of students per month in 2018'
options['theme'] = 'default'


# create ColorEx object, passing options.
colorex_grid = ColorExGrid(options)

# create color grid in HTML
colorex_grid.to_html('attendance.html',
    'templates\\template.html')

