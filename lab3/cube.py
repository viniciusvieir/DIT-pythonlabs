# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 15:18:19 2018

@author: D16129083
"""

def calculate_cube(width):
    
    for k in range(1, width + 1):
        
        volume = k ** 3
        surface_area = 6 * k ** 2
        
        if volume == surface_area:
            print('Width:', k, 'SA:', surface_area, 'Volume:', volume, '- MATCH FOUND!!!')
        else:
            print('Width:', k, 'SA:', surface_area, 'Volume:', volume, '- Not a match!')

def main():
    calculate_cube(int(input('Type the width of the cube as a positive integer: ')))

main()
