n1 = int(input("Enter the first number : "))
n2 = int(input("Enter the second number : "))

miniMum = min(n1 , n2)

for i in range(1,miniMum+1):
    if n1%i ==0 and n2%i == 0:
        hcf = i
print(f"The HCF of {n1} and {n2} is", hcf)