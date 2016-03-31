#!/usr/bin/python3

class Numbers(object):
    """Numbers class"""
        
    def print_numbers():
        stack = []
        for number in range(1,101):
            if number % 3 == 0 and number % 5 == 0:
                stack.append("ThreeFive")
            elif number % 3 == 0:
                stack.append("Three")
            elif number % 5 == 0:
                stack.append("Five")
            else:
                stack.append(number)
        return stack
