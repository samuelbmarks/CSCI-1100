'''
Write a function called add_tuples that takes three tuples, each with two values, and returns a single tuple with two values containing the sum of the values in the tuples.
Author: Samuel Marks
CSCI1100 Spring 2018
Version 1
'''

def add_tuples( x, y, z ):
    x_total = x[0] + y[0] + z[0]
    y_total = x[1] + y[1] + z[1]
    return (x_total, y_total)

print(add_tuples( (1,4), (8,3), (14,0) ))
print(add_tuples( (3,2), (11,1), (-2,6) ))