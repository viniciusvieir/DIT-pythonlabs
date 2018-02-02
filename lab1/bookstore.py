# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 16:44:35 2018

@author: D16129083
"""

coverPrice = input("What's the price of the cover book: ")
numberOfCopies = input("How many copies do you need: ")


discount = 0.4

initialShipping = 3.0
extraShipping = 0.75

totalCover = (float(coverPrice) - (float(coverPrice) * discount)) * int(numberOfCopies)
totalExtraShipping = (int(numberOfCopies) - 1) * extraShipping

total = totalCover + initialShipping + totalExtraShipping

print("The total of the order is", total)

# Item 9 - The total wholesale cost fot 60 copies is 945.4499999999999

