#1. Write a Python program to find sum of elements in list?

lst = []


n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input("enter the elements : "))

    lst.append(ele)  # adding the element

print(lst)
# Calculate sum of list
numsum=0
for i in lst:
    numsum+=i
print('Sum of List: ', numsum)

