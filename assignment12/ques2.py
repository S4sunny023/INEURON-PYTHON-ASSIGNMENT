#2. Write a Python program to find the sum of all items in a dictionary?


def sum_dict_values(d):
    """
    Returns the sum of all values in a dictionary.
    """
    return sum(d.values())

n = int(input("enter a n value:"))
d = {}


for i in range(n):
    keys = input("enter keys : ") 
    values = int(input("enter values: ")) 
    d[keys] = values
print(d)
print(sum_dict_values(d)) 
