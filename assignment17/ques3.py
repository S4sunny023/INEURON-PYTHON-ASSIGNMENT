'''
Question3. Create a function that replaces all the vowels in a string with a specified character.
Examples
replace_vowels("the aardvark", "#") ➞ "th# ##rdv#rk"

replace_vowels("minnie mouse", "?") ➞ "m?nn?? m??s?"

replace_vowels("shakespeare", "*") ➞ "sh*k*sp**r*"
'''

def replace_vowels(string, char):
    vowels = "AEIOUaeiou"
    for vowel in vowels:
        string = string.replace(vowel, char)
    return string

print(replace_vowels("hello world", "*"))


