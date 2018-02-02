# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
EXERCISE 1
    It does not make a difference if the input numbers are ints or floats,
     as the variable average handles it properly. 
    If the output result gets converted to a float the print statement is the same
     because the variable is already treated as a float. If it gets casted to a int
     then the result gets rounded down to the closest int.
"""

number1 = 3.0
number2 = 5
number3 = 6

average = (number1 + number2 + number3) / 3

print("The average of these three numbers is", int(average))