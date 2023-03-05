Number = int(input("Enter the Number to Check Harshad Number = "))
Sum = 0
rem = 0

Temp = Number
while Temp > 0:
    rem = Temp % 10
    Sum = Sum + rem
    Temp = Temp // 10

print("The Sum of the Digits = %d" %Sum)

if Number % Sum == 0:
    print("\n%d is a Harshad Number." %Number)
else:
    print("%d is Not a Harshad Number." %Number)