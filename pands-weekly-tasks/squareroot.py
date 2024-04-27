# Write a program that takes a positive floating-point 
# number as input and outputs an approximation of its square root.
# Author : Andre Machado

import math


def squareroot():
    a = float(input("Please enter a positive number: "))
    x = math.sqrt(a)
    
    print(f"The square root of {a} is approx {x:.1f}")

squareroot()
