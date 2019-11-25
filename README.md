# ColorEx Library

*ColorEx* is a data visualization library that uses color creatively to represent data, make visualization interactive, and ultimately be a great tool for learning patterns in data.

## Features

- Supports CSV data input.
- Generates color grid in HTML format.
- Single-colored and multi-colored tile grids supported.


## Requirements

- Python 3.7+

## Installation

#### Install from PyPi (recommended)

```shell
$ pip install colorex
```



## Get Started

Here is a simple example to get you started;

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

See [Contributing.md](CONTRIBUTING.md) to learn how you can contribute to this project.

## License

ColorEx is licensed under MIT License.