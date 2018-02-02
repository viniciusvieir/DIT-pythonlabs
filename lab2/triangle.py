# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 15:25:44 2018

@author: D16129083
"""

"""
EXERCISE 3
    -- CODE --

EXERCISE 4
    If the triangle sides are 3 and 4 the hypotenuse is 5.0.
    If the triangle sides are -3 and -4 the hypotenuse is also 5.0.
"""

from math import sqrt

opposite_side = input('Whats the opposite side of the triangle: ')
adjacent_side = input('Whats the adjacent side of the triangle: ')

hypotenuse = sqrt( float(opposite_side) ** 2 + float(adjacent_side) ** 2 )

print('The hypotenuse of the triangle is', hypotenuse)