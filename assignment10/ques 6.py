#  Write a Python program to find N largest elements from a list?

def N_max_elements(list, N):
    result_list = []

    for i in range(0, N):
        maximum = 0

        for j in range(len(list)):
            if list[j] > maximum:
                maximum = list[j]

        list.remove(maximum)
        result_list.append(maximum)

    return result_list


# test
lst = []


n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input("enter the elements : "))

    lst.append(ele)  # adding the element

print(lst)
N = int(input("enter the N no. of element: "))

print(N, "max elements in ", lst)

# Calling and printing the function
print(N_max_elements(lst, N))