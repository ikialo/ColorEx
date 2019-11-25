# ColorEx Library

*ColorEx* is a data visualization library that uses color expressively to represent data, make visualization interactive, and ultimately be a great tool for learning patterns in data. ColorEx is simple.

## Features

- Supports CSV, JSON, XML data file input. 
- Colored tile grid formats in HTML, PNG, JPG, PDF.
- Single-colored and multi-colored tile grids.

## Documentation

More detailed documentation of the library is available at [Colorex Documentation](https://www.google.com.pg)

## Requirements

- Python 3.7 or later.
- Cheetah

## Installation

#### Install from PyPi (recommended)

```shell
$ pip install colorex
```



## Get Started

Get started quickly by first copying this to a new Python file, and running it in your interpreter;

```python
import colorex as cx

csvFile = cx.CSVReader('website_traffic.csv')
dataGrid = csvFile.generate_datagrid()


engine = cx.ColorEx({
    'default-rgb': '000000',
    'rgbs': ['000000']
})

tileGrid = engine.generate_tilegrid(dataGrid)

HTMLOutputFile = cx.HTMLWriter('Website Traffic.html', tileGrid)
HTMLOutputFile.write({'template': 'default'})

```



## Contributing

See [Contributing](CONTRIBUTING.md) to learn more about how to contribute to this project.



## License

Copyright (c) 2019. Louis Ronald.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.