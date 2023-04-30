#4. Write a Python Program to Split the array and add the first part to the end?

def split_and_add(arr, n):
    part1 = arr[:n]
    part2 = arr[n:]

    new_arr = part2 + part1

    return new_arr

array = [1, 2, 3, 4, 5]
n = 2
new_array = split_and_add(array, n)
print("Original Array:", array)
print("New Array:", new_array)
