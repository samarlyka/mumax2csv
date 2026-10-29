# mumax2csv

Converts Mumax3 data table to CSV format

## Features

Allows Mumax3 data table to be parsed by various data processing programs other than [gnuplot](https://sourceforge.net/projects/gnuplot).

## Installation

To run `mumax2csv`, simply install the latest Python version from https://www.python.org/downloads and execute the following command to download `mumax2csv` from Python Package Index (PyPI):

```sh
pip install mumax2csv
```

## Usage

To convert a Mumax3 data table file into CSV, execute the following from the command line/terminal:

```sh
python -m mumax2csv path/to/mumax3/datatable.txt
```

Glob pattern and multiple file arguments are also supported:

```sh
#!/bin/bash
# Using the UNIX Glob pattern:
python -m mumax2csv path/to/mumax3/*.txt

# Specifying multiple data table files:
python -m mumax2csv table1.txt table2.txt table3.txt
```

You can also specify whether the unit name of each column in the data table file should be preserved. This can be achieved by accessing the `keep_unit` parameter in the converter. The default behavior is `False` (i.e., omitting the unit name altogether). If you set `keep_unit` to `True`, the second row of the output CSV file will keep the unit name information.

Examples on how to set the `keep_unit` parameter via the terminal:

```sh
python -m mumax2csv -k 1 table.txt
python -m mumax2csv --keep-unit false table.txt
# "1" for "true", "0" for "false".
```

An example on how to set the `keep_unit` parameter by importing the Python module:

```python
import mumax2csv
mumax2csv.convert(
    file_input='path/to/mumax3/datatable.txt',
    keep_unit=False
)
```
