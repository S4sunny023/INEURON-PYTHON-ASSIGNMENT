'''
Question 2.Create a function that takes an angle in radians and returns the corresponding angle in degrees rounded to one decimal place.
Examples
radians_to_degrees(1) ➞ 57.3

radians_to_degrees(20) ➞ 1145.9

radians_to_degrees(50) ➞ 2864.8'''

import math

def radians_to_degrees(radians):
    degrees = radians * (180 / math.pi)
    return round(degrees, 1)



radians = 20
degrees = radians_to_degrees(radians)
print(degrees)