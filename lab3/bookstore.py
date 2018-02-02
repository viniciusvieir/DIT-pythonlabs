# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 16:44:35 2018

@author: D16129083
"""

def get_total(coverPrice, numberOfCopies):

    discount = 0.4

    initialShipping = 3.0
    extraShipping = 0.75
        
    totalCover = (coverPrice - (coverPrice * discount)) * numberOfCopies
    totalExtraShipping = (numberOfCopies - 1) * extraShipping

    total = totalCover + initialShipping + totalExtraShipping
    
    return total

def main():
    coverPrice = float(input("What's the price of the cover book: "))
    numberOfCopies = int(input("How many copies do you need: "))
    print("The total of the order is", get_total(coverPrice, numberOfCopies))

main()

