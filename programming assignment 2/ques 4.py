import cmath

print("General form :ax**2+bx+c = 0")
a = int(input("Enter a (a!=0): "))
b = int(input("enter b :"))
c = int(input('enter c: '))

D = (b**2)-(4*a*c)

sol1 = (-b-cmath.sqrt(D))/(2*a)
sol2 = (-b+cmath.sqrt(D))/(2*a)


print(f"Results for equation, {a}x**2 + {b}x + {c} = 0, are :" )
if D>0:
    print("type of roots : Two Distinct Real Roots ")
elif D == 0:
    print("type of roots : Two Equal Roots" )
elif D < 0:
    print("type of roots :  Two Complex Roots")

print(f"the solution are {sol1} and {sol2} ")
