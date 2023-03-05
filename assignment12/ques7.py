#7. Write a Python program to sort Python Dictionaries by Key or Value?

n = int(input("enter a n value:"))
d = {}


for i in range(n):
    keys = input("enter keys : ") 
    values = int(input("enter values: ")) 
    d[keys] = values
print(d)

myKeys = list(d.keys())
myKeys.sort()
sorted_dict = {i: d[i] for i in myKeys}

print(sorted_dict)
