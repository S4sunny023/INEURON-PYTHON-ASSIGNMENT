#3. Write a Python Program for array rotation?

def rotate_array(arr, k):
    n = len(arr)
    k = k % n
    arr = arr[k:] + arr[:k]

    return arr

array = [1, 2, 3, 4, 5]
k = 2
rotated_array = rotate_array(array, k)
print("Original Array:", array)
print("Rotated Array:", rotated_array)
