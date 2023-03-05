'''Question 3
Create a function that squares every digit of a number.
Examples
square_digits(9119) ➞ 811181

square_digits(2483) ➞ 416649

square_digits(3212) ➞ 9414
Notes
The function receives an integer and must return an integer.'''

def square_digits(num):
    result = ""
    for digit in str(num):
        result += str(int(digit)**2)
    return int(result)

print(square_digits(9119))
print(square_digits(2483))
print(square_digits(3212))
