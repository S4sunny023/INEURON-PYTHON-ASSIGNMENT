#3. Write a Python program to Merging two Dictionaries?


def merge_dicts(d1, d2):
    """
    Returns a new dictionary that is the result of merging two dictionaries.
    """
    merged_dict = d1.copy()
    merged_dict.update(d2)
    return merged_dict


n1 = int(input("enter a n1 value:"))
d1 = {}

for i in range(n1):
    keys = input("enter keys : ") 
    values = int(input("enter values: "))
    d1[keys] = values
print(d1)

n2 = int(input("enter a n2 value:"))
d2 = {}

for i in range(n2):
    keys = input("enter keys : ") 
    values = int(input("enter values: "))
    d1[keys] = values
print(d1)

merged_dict = merge_dicts(d1, d2)
print(merged_dict)  
