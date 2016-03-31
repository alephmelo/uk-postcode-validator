#!/usr/bin/python3

import unittest
from main import Validator
from numbers import Numbers

class TestValidator(unittest.TestCase):
    def test_postcodes_validated_ok(self):
        self.assertTrue(Validator.is_valid('SW1A 1AA'))


    def test_postcodes_validated_also_ok(self):
        self.assertTrue(Validator.is_valid('SW1A1AA'))


    def test_postcodes_validated_not_ok(self):
        self.assertFalse(Validator.is_valid('XXX 9AA'))


class TestNumbers(unittest.TestCase):

    stack = [1, 2, 'Three', 4, 'Five', 'Three', 7, 8, 'Three', 'Five',\
            11, 'Three', 13, 14, 'ThreeFive', 16, 17, 'Three', 19, 'Five', \
            'Three', 22, 23, 'Three', 'Five', 26, 'Three', 28, 29, 'ThreeFive',\
            31, 32, 'Three', 34, 'Five', 'Three', 37, 38, 'Three', 'Five', \
            41, 'Three', 43, 44, 'ThreeFive', 46, 47, 'Three', 49, 'Five', \
            'Three', 52, 53, 'Three', 'Five', 56, 'Three', 58, 59, 'ThreeFive',\
            61, 62, 'Three', 64, 'Five', 'Three', 67, 68, 'Three', 'Five',\
            71, 'Three', 73, 74, 'ThreeFive', 76, 77, 'Three', 79, 'Five',\
            'Three', 82, 83, 'Three', 'Five', 86, 'Three', 88, 89, 'ThreeFive',\
            91, 92, 'Three', 94, 'Five', 'Three', 97, 98, 'Three', 'Five']

    def test_numbers_ok(self):
        self.assertEqual(Numbers.print_numbers(), self.stack)


if __name__ == '__main__':
    unittest.main()
