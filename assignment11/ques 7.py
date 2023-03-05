#7. Write a Python Program to check if a string contains any special character?

import re


def run(string):

    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')


    if (regex.search(string) == None):
        print("it has not any special chr")

    else:
        print("it has special chr")

if __name__ == '__main__':

    string = input("enter the string: ")


    run(string)
