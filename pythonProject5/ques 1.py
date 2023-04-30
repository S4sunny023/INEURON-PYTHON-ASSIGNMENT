a = int(input("Enter the first number :"))
b = int(input("Enter the second number :"))
maxNum = max(a, b)
while(True):
    if (maxNum%a==0 and maxNum%b == 0):
        break
    maxNum = maxNum+1
print(f"the lcm of {a} and {b} is {maxNum}")

