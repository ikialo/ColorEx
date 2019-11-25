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

Ideas, bugs, tests, and pull requests are always welcome for the project.

We have a curated list of issues and or development targets for *ColorEx* made available on the [ColorEx Wiki](https://www.google.com.pg). 

If you're interested in developing *ColorEx* further, pick a subject from the list and open a Pull Request for it. If you are adding a feature that is not captured in that list yet, consider if the work for it could also contribute towards delivering any of the existing todo items too. 



## License

This project is licensed under MIT License.