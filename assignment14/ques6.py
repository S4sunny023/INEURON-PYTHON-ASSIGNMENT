'''
Question 6:
Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.

'''

def binary_search(sorted_list, item):
    """Perform binary search for item in sorted_list."""
    first = 0
    last = len(sorted_list) - 1
    
    while first <= last:
        midpoint = (first + last) // 2
        if sorted_list[midpoint] == item:
            return midpoint
        elif sorted_list[midpoint] > item:
            last = midpoint - 1
        else:
            first = midpoint + 1
    
    # Item not found in the list
    return -1




sorted_list=[]
n = int(input("Enter number of elements : "))


for i in range(0, n):
	ele = int(input("enter the elemnts:"))

	sorted_list.append(ele) # adding the element
	


item=int(input("enter your item :"))

print(binary_search(sorted_list, item))

