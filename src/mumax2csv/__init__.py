"""
mumax2csv
Created by: Samarthya Lykamanuella
Establishment year: 2026

This program converts Mumax3-generated data table into CSV format.

LICENSE NOTICE:
===============

MIT License

Copyright (c) 2026 Samarthya Lykamanuella

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# For separating filenames/paths.
# (Default package from Python installation. No PIP extension required.)
import os


def despacifier(str_):
    """
    A simple function that removes redundant (double) space characters.
    """
    # Ensures tabs are replaced with spaces accordingly.
    str_ = str_.strip().replace('\t', ' ')
    
    while str_.__contains__('  '):
        str_ = str_.replace('  ', ' ')
    
    # Ensures that the string does not start or end in blank spaces
    str_ = str_.strip()
    return str_

def remove_empty(input_list=[]):
    """
    Remover of empty list items or list items with only blank spaces.
    Assumes each item in input_list is a string.
    """
    # The new list
    output_list = []
    
    # Read the input list/array
    for a in input_list:
        l = a.strip()
        if len(l) == 0:
            # The list item is empty
            # No need to append to the new list
            pass
        else:
            # You've made it, item list!
            output_list.append(l)
    
    # Return the sanitized list
    return output_list

def space2comma(str_):
    """
    Turn all space characters into commas.
    """
    # Despacify!
    str_ = despacifier(str_)
    # Convert spaces to commas
    str_ = str_.replace(' ', ',')
    return str_

def convert(file_input: str, csv_output: str = None, output_suffix: str = None, keep_unit: bool = False):
    """
    Performs the data table conversion.
    """
    
    # Detecting if input file exists.
    if not os.path.exists(file_input):
        raise Exception(f'File not found: {file_input}')
    
    # Determining the output CSV path.
    if csv_output is None and output_suffix is None:
        fo = os.path.splitext(file_input)[0] + '.csv'
    elif csv_output is None and output_suffix is not None:
        fo = os.path.splitext(file_input)[0] + str(output_suffix) + '.csv'
    else:
        fo = csv_output
        # Ensuring that the filename always ends in 'csv'.
        if fo[-4:] != '.csv':
            fo += '.csv'
    
    # Reading the input file.
    read_in = open(file_input, 'r')
    
    # Setting up the writer.
    open(fo, 'w').close()
    write_out = open(fo, 'a')
        
    # Reading the input file to convert.
    for l in read_in:
            
        # Stripping redundant blank chars.
        l = despacifier(l)
        
        # Column/data header.
        if l.startswith('#'):
            column_names = [n for n in l.replace('#', '').strip().split() if not n.__contains__('(')]
            write_out.write(space2comma(' '.join(column_names)) + '\n')
            
            # Adding unit information.
            if keep_unit:
                units = ['a.u.' if u == '' else u for u in [u.split('(')[1] for u in remove_empty(l.split(')'))]]
                write_out.write(space2comma(' '.join(units)) + '\n')
        
        # Data rows
        else:
            write_out.write(space2comma(l) + '\n')
            continue
        
    # Closing the writer.
    write_out.close()
    
    # Closing the reader.
    read_in.close()
