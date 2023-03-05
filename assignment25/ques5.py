'''Question5
Create a function that takes a string as input and capitalizes a letter if its ASCII code is even and returns its lower case version if its ASCII code is odd.
Examples
ascii_capitalize("to be or not to be!") ➞ "To Be oR NoT To Be!"

ascii_capitalize("THE LITTLE MERMAID") ➞ "THe LiTTLe meRmaiD"

ascii_capitalize("Oh what a beautiful morning.") ➞ "oH wHaT a BeauTiFuL moRNiNg."'''


def ascii_capitalize(word):
    result = ""
    for letter in word:
        if ord(letter) % 2 == 0:
            result += letter.upper()
        else:
            result += letter.lower()
    return result

print(ascii_capitalize("to be or not to be!"))
print(ascii_capitalize("THE LITTLE MERMAID") )
print(ascii_capitalize("Oh what a beautiful morning."))













