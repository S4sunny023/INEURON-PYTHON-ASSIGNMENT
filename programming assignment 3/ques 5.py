l = 1
u = 10000

for i in range (l, u+1):
    if (i>1):
        for j in range(2,i):
            if (i%j)==0:
                break
        else:
            print(i)
