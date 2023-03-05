#1. Write a Python program to check if the given number is a Disarium Number?
def is_disarium(num):
    temp = n
    for i in range(len(str(num))):
        temp += int(str(num)[i]) ** (i + 1)
    return temp == num

n= int(input("enter the digit:"))
print( is_disarium(n))
