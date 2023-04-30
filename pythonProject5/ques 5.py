num1 = int(input("Enter the first value :"))
num2 = int(input("Enter the second value :"))
opr =  input("Enter the operator sign( + , - , * , /):" )
if opr == "+":
    print(num1 + num2)
elif opr == "-":
    print(num1-num2)
elif opr == "*":
    print(num1*num2)
elif opr == "/":
    print(num1/num2)
else:
    print("Invalid operator")
