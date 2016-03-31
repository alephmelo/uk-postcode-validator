# UK Postcode Validator [![Build Status](https://travis-ci.org/alephmelo/uk-postcode-validator.svg?branch=master)](https://travis-ci.org/alephmelo/uk-postcode-validator)
A comprehensive postcode validator library using Python 3.

# Installation
Open your terminal and clone the repository from here:
```bash
$ git clone git@github.com:alephmelo/uk-postcode-validator.git
$ cd uk-postcode-validator
$ python3 setup install
```

Or save you some time and just download it the package as zip file, your choice.

# Usage
Once you have the package installed just import inside a python interpreter.

```bash
$ python3
```
```python
>>> from validator.main import Validator
>>> Validator.is_valid('SW1A1AA')
True
```

# Tests
To run tests just execute the `tests.py` file.

```bash
$ python3 tests.py
....
----------------------------------------------------------------------
Ran 4 tests in 0.003s

OK

```

# Demo
![Image](../master/assets/demo.gif?raw=true)

# Bonus
```python
>>> from validator.numbers import Numbers
>>> Numbers.print_numbers()
[1, 2, 'Three', 4, 'Five', 'Three', 7, 8, 'Three', 'Five', 11, 'Three', 13, 14, 'ThreeFive', 16, 17, 'Three', 19, 'Five', 'Three', 22, 23, 'Three', 'Five', 26, 'Three', 28, 29, 'ThreeFive', 31, 32, 'Three', 34, 'Five', 'Three', 37, 38, 'Three', 'Five', 41, 'Three', 43, 44, 'ThreeFive', 46, 47, 'Three', 49, 'Five', 'Three', 52, 53, 'Three', 'Five', 56, 'Three', 58, 59, 'ThreeFive', 61, 62, 'Three', 64, 'Five', 'Three', 67, 68, 'Three', 'Five', 71, 'Three', 73, 74, 'ThreeFive', 76, 77, 'Three', 79, 'Five', 'Three', 82, 83, 'Three', 'Five', 86, 'Three', 88, 89, 'ThreeFive', 91, 92, 'Three', 94, 'Five', 'Three', 97, 98, 'Three', 'Five']

```