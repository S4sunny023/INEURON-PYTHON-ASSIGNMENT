'''Question1
Create a function that takes a string and returns a string in which each character is repeated once.
Examples
double_char("String") ➞ "SSttrriinngg"

double_char("Hello World!") ➞ "HHeelllloo  WWoorrlldd!!"

double_char("1234!_ ") ➞ "11223344!!__  " '''

def double_char(txt):
    result = ''
    for char in txt:
        result += char * 2
    return result

print(double_char("String")) 
print(double_char("Hello World!"))
print(double_char("1234!_ ")) 
