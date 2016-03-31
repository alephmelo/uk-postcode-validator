#!/usr/bin/python3
import re


class Validator(object):
	"""Validator class"""

	def is_valid(postcode):
		"""Given a postcode and check whether is valid or not valid.

		Args:
            postcode (str): The postcode to be checked.

        A valid postcode can be with or without a space char in between. 
        Like: 'SW1A 1AA' or 'SW1A1AA' are both considered valid."""

		inw = 'ABDEFGHJLNPQRSTUWXYZ'
		fst = 'ABCDEFGHIJKLMNOPRSTUWYZ'
		sec = 'ABCDEFGHKLMNOPQRSTUVWXY'
		thd = 'ABCDEFGHJKSTUW'
		fth = 'ABEHMNPRVWXY'

		if re.match('[%s]\d ?\d[%s][%s]$' % (fst, inw, inw), postcode) or \
		    re.match('[%s]\d\d ?\d[%s][%s]$' % (fst, inw, inw), postcode) or \
		    re.match('[%s][%s]\d ?\d[%s][%s]$' % (fst, sec, inw, inw), postcode) or \
		    re.match('[%s][%s]\d\d ?\d[%s][%s]$' % (fst, sec, inw, inw), postcode) or \
		    re.match('[%s]\d[%s] ?\d[%s][%s]$' % (fst, thd, inw, inw), postcode) or \
		    re.match('[%s][%s]\d[%s] ?\d[%s][%s]$' % (fst, sec, fth, inw, inw), postcode):
		    return True

		return False
