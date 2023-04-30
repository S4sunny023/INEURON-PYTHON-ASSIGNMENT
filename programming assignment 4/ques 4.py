n = int(input("enter the number : "))
sum = 0
order = len(str(n))
copy_n = n
while (n>0):
    digit = n%10
    sum = sum + digit** order
    n = n//10
if sum == copy_n:
    print(copy_n,"armstrong number")
else:
    print(copy_n,"not an armstrong number")