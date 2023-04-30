n = int(input("Enter the natural number till you want to sum :"))
sum = 0
for i in range(1,n+1):
    sum = sum + (i**3)
print(f"sum of first {n} natural number is {sum} ")