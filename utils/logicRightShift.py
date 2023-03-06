# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 12:32:52 2020

@author: chenxy

Reference:
    https://stackoverflow.com/questions/5832982/how-to-get-the-logical-right-binary-shift-in-python/5833010#5833010
In Python,
    The modulo operator always yields a result with the same sign as its second
    operand (or zero).

"""


def rshift(val, n):
    # Assuming the integer is represents with 32 bits.
    return val >> n if val >= 0 else (val+0x100000000) >> n


def rshift1(val, n):
    # Assuming the integer is represents with 32 bits.
    # An improvement upon rshift
    return (val % 0x100000000) >> n


if __name__ == '__main__':
    print('expect = 536870787, actual = {0}'.format(rshift(-1000, 3)))
    print('expect = 125, actual = {0}'.format(rshift(-1000, 3)))

    print('expect = 536870787, actual = {0}'.format(rshift1(-1000, 3)))
    print('expect = 125, actual = {0}'.format(rshift1(-1000, 3)))
