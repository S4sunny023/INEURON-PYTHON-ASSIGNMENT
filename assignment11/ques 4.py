#4. Write a Python to check if a given string is binary string or not?

def check(s):
    binary = "01"
    flag=0
    for char in s:
        if char not in binary:
            flag=1
            break
        else:
            pass
    if flag==1:
        print("Not binary")
    else:
        print("Binary")


s = input("enter your string:")

print(check(s))