#9. Write a Python program to Remove empty List from List?

# Python3 Code to Demonstrate Remove empty List
# from List using filter() Method


test_list = [5, 6, [], 3, [], [], 9]


print("The original list is : " + str(test_list))

res = list(filter(None, test_list))

print("List after empty list removal : " + str(res))
