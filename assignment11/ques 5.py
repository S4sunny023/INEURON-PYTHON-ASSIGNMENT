#5. Write a Python program to find uncommon words from two Strings?


def UncommonWords(A, B):
    A = A.split()
    B = B.split()
    x = []
    for i in A:
        if i not in B:
            x.append(i)
    for i in B:
        if i not in A:
            x.append(i)
    x = list(set(x))
    return x


# Driver Code
A = input("enter your first sentence: ")

B = input("enter your second sentence: ")

# Print required answer
print(UncommonWords(A, B))
