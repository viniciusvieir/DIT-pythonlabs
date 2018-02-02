# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 17:01:01 2018

@author: D16129083
"""

euroToPoundsRate = 1.1478

ammount = input("Type the ammount of pounds you want to convert to euro? ")

euros = float(ammount) * euroToPoundsRate

print(ammount, "pounds is", euros, "euros")