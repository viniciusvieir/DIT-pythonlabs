# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 15:30:30 2018

@author: D16129083
"""

"""
EXERCISE 5
    -- CODE --

EXERCISE 6
    It is good practice to use very descriptive variable/methods names. 
    I created some methods to check if the input data is a number, so the program
    doesn't crash when it comes to calculations.
"""

# This method checks if the value inputed by the user is a number, otherwise it
# calls the method again
def get_user_input(title):
    input_value = input(title)  
    if isInt(input_value) or isFloat(input_value):
        return input_value
    else:
        print('Please type a value with the right format.')
        return get_user_input(title)

# This method checks if some value is a float
def isFloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# This method checks if some value is an int    
def isInt(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
    

# Here all the information are gatheed from the user
age = get_user_input('What is your age? ')
weight = get_user_input('What is you weight in kgs? ')
height = get_user_input('What is your height in cms? ')
    
# All calculations happens here based on the user's info
dog_years = int(age) / 7

weight_on_moon = float(weight) * .17
weight_on_sun = float(weight) * 27.07

weight_in_pounds = float(weight) / 0.45359237

height_in_inches = float(height) * 0.39370079

bmi = float(weight) / float(height) ** 2 * 10000

# All the infomation are displayed using the print statement
print('-'*60)
print('Your age in dog years is', format(dog_years, '.0f'))

print('Your weight on the moon is ' + format(weight_on_moon, '.1f') + ' kgs and '+
      format(weight_on_sun, '.1f') + ' kgs on the sun.')

print('Your weight in pounds is ' + format(weight_in_pounds, '.1f') + ' pounds.')
print('Your height in inches is ' + format(height_in_inches, '.0f') + ' inches.')

print('You BMI (Body Mass Index) is ' + format(bmi, '.1f'))
print('-'*60)

