#2. Write a Python program for removing i-th character from a string?
def remove(string,i):

	for j in range(len(string)):
		if j == i:
			string = string.replace(string[i], "", 1)
	return string


s = input("enter word: ")


if __name__ == '__main__':

	string = s


	i =int(input('Remove with index element: '))


	print(remove(string, i))
