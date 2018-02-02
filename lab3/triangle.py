# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 15:25:44 2018

@author: D16129083
"""

from math import sqrt

def get_input(side):
    
    value = input('Whats the ' + side + ' side of the triangle: ')
    
    if not is_number(value):
        print('Please type a number.')
        return get_input(side)
    
    value = float(value)
    
    if value < 0:
        print('Please type a positive value.')
        return get_input(side)
    else:
        return value

def is_number(value):
    try:
        float(value)
        return True
    except (ValueError):
        return False
    
    try:
        from unicodedata import numeric
        numeric(value)
        return True
    except (TypeError, ValueError):
        return False

def calculate_hypotenuse(x, y):    
    return sqrt( x ** 2 + y ** 2 )

def main():
    x = get_input('opposite')
    y = get_input('adjacent')
    
    print('The hypotenuse of the triangle is', format(calculate_hypotenuse(x, y), '.4f'))

main()