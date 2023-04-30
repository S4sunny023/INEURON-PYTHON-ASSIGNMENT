#2. Write a Python Program to find largest element in an array?

array = [1, 5, 3, 7, 2]
max = array[0]


for i in range(1, len(array)):
    if array[i] > max:
        max = array[i] 

print("Largest element in the array:", max)
