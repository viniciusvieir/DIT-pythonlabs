# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 16:35:35 2018

@author: D16129083
"""

def harmonic(n):
    total = 0
    for k in range(1, n+1):
        total += 1/k
    return total

def main():
    n = int(input('Enter a positive integer: '))
    print('The sum of 1/k for k = 1 to', n, 'is', format(harmonic(n), '.1f'))
    
main()