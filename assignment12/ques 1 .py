#1. Write a Python program to Extract Unique values dictionary values?


number = int(input("enter no. value:"))

dict = {}


name = input("enter the key :")

values = input("enter the values :")

dict[name] = values
print(dict)
print("The original dictionary is : " + str(dict))

# Extract Unique values dictionary values
x=[]
for i in dict.keys():
	x.extend(dict[i])
x=list(set(x))
x.sort()
# printing result
print("The unique values list is : " + str(x))
