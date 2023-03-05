'''Question1
Create a function that takes a list of strings and integers, and filters out the list so that it returns a list of integers only.
Examples
filter_list([1, 2, 3, "a", "b", 4]) ➞ [1, 2, 3, 4]

filter_list(["A", 0, "Edabit", 1729, "Python", "1729"]) ➞ [0, 1729]

filter_list(["Nothing", "here"]) ➞ []
'''
def filter_list(lst):
    integers_only = []
    for item in lst:
        if isinstance(item, int):
            integers_only.append(item)
    return integers_only

print(filter_list([1, 2, 3, "a", "b", 4]))


print(filter_list(["A", 0, "Edabit", 1729, "Python", "1729"]))


print(filter_list(["Nothing", "here"]))
