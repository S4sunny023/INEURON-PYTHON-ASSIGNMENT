#Write a Python program to find smallest number in a list?

lst = []


n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input("enter the elements : "))

    lst.append(ele)  # adding the element

print(lst)
lst.sort()
print("Smallest element is:", lst[0])
