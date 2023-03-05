#3. Write a Python program to split and join a string?

def split_string(string):

    lst_string = string.split(' ')

    return lst_string

def join_string(lst_string):

    string = '-'.join(lst_string)

    return string

s = input("enter the line: ")

if __name__ == '__main__':
    string = s


    lst_string = split_string(string)
    print(lst_string)


    new_string = join_string(lst_string)
    print(new_string)
