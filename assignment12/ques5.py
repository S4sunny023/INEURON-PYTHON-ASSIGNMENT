#5. Write a Python program to insertion at the beginning in OrderedDict?

from collections import OrderedDict

def insert_at_beginning(ordered_dict, key, value):
    """
    Inserts a new key-value pair at the beginning of an OrderedDict.
    """
    # Create a new OrderedDict with the new key-value pair at the beginning
    new_dict = OrderedDict([(key, value)])
    new_dict.update(ordered_dict)
    return new_dict

n = int(input("enter a n value:"))
d = {}


for i in range(n):
    keys = input("enter keys : ") 
    values = int(input("enter values: ")) 
    d[keys] = values
print(d)


ordered_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
new_dict = insert_at_beginning(ordered_dict, 'x', 100)
print(new_dict) 

