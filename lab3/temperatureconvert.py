# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 17:07:43 2018

@author: D16129083
"""

def get_fahrenheit(celsius):
    return float(celsius) * 9/5 + 32

def main():
    celsius = float(input("The the temperature in Celsius: "))
    fahrenheit = get_fahrenheit(celsius)
    print(celsius, "celsius is equivalent to", fahrenheit, "fahrenheit")

main()

