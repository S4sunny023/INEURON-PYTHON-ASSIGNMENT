#2. Write a Python program to Multiply all numbers in the list?


lst = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input("enter the elements : "))

    lst.append(ele)  # adding the element

print(lst)
# Calculate sum of list
result = 1
for i in lst:
   result = result * i
print('Sum of List: ',result)

