#6. Write a Python program to check order of character in string using OrderedDict()?

from collections import OrderedDict

def check_char_order(string, pattern):
    """
    Checks whether the characters in the string appear in the same order as the characters in the pattern.
    """
    
    pattern_dict = OrderedDict.fromkeys(pattern)

    
    for char in string:
        
        if char in pattern_dict:
            pattern_dict.popitem(last=False)

   
    return len(pattern_dict) == 0


string = input("enter the string : ")
pattern = input("enter pattern : ")
result = check_char_order(string, pattern)
print(result) 
