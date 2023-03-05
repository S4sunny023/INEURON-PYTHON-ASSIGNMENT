'''Question 4.Given the side length x find the area of a hexagon.
 
Examples
area_of_hexagon(1) ➞ 2.6

area_of_hexagon(2) ➞ 10.4

area_of_hexagon(3) ➞ 23.4
'''


import math

def area_of_hexagon(x):
    area = (3 * math.sqrt(3) * x ** 2) / 2
    return area


x= int(input("enter the side: "))

print(area_of_hexagon(x))