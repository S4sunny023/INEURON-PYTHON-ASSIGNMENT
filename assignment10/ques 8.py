#8. Write a Python program to print odd numbers in a List?

lst = []


n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input("enter the elements : "))

    lst.append(ele)  # adding the element

print(lst)

for i in lst:
    if i % 2  != 0:

	    print(i)
