n = int(input("Enter thr number of sequence :"))
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)
for i in range(0,n+1):
    print(fib(i))


