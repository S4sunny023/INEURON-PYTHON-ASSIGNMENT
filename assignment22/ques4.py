'''Question4
An isogram is a word that has no duplicate letters. Create a function that takes a string and returns either True or False depending on whether or not it's an "isogram".
Examples
is_isogram("Algorism") ➞ True

is_isogram("PasSword") ➞ False
# Not case sensitive.

is_isogram("Consecutive") ➞ False
Notes
•	Ignore letter case (should not be case sensitive).
•	All test cases contain valid one word strings.
'''

def is_isogram(word):
    return len(set(word.lower())) == len(word)


print(is_isogram("Algorism"))
print(is_isogram("PasSword"))
print(is_isogram("Consecutive"))
