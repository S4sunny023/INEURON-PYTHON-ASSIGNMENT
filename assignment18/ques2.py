'''Question 2
The "Reverser" takes a string as input and returns that string in reverse order, with the opposite case.
Examples
reverse("Hello World") ➞ "DLROw OLLEh"

reverse("ReVeRsE") ➞ "eSrEvEr"

reverse("Radar") ➞ "RADAr"'''

def reverse(txt):
    new_txt = ""
    for char in txt[::-1]:
        if char.islower():
            new_txt += char.upper()
        elif char.isupper():
            new_txt += char.lower()
        else:
            new_txt += char
    return new_txt

print(reverse("Hello World"))  
print(reverse("ReVeRsE")) 
print(reverse("Radar"))  
