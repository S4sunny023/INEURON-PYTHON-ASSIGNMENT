'''Question 5
Write a function that moves all elements of one type to the end of the list.
Examples
move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]
# Move all the 1s to the end of the array.

move_to_end([7, 8, 9, 1, 2, 3, 4], 9) ➞ [7, 8, 1, 2, 3, 4, 9]

move_to_end(["a", "a", "a", "b"], "a") ➞ ["b", "a", "a", "a"]
'''

def move_to_end(lst, elem):
    
    not_elem_lst = []
    elem_lst = []
  
    for e in lst:
        if e != elem:
            not_elem_lst.append(e)
        else:
            elem_lst.append(e)
   
    return not_elem_lst + elem_lst

print(move_to_end([1, 3, 2, 4, 4, 1], 1)) 
print(move_to_end([7, 8, 9, 1, 2, 3, 4], 9)) 
print(move_to_end(["a", "a", "a", "b"], "a")) 
