# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 17:10:29 2018

@author: D16129083
"""

def cube_info(width, length):
    return width * length

def main():
    width = float(input("Type the width of the rectangle: "))
    length = float(input("Type the lenth of the rectangle: "))

    print("The area of the rectangle is", cube_info(width, length))

main()