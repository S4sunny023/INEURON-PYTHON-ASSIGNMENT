#6. Write a Python to find all duplicate characters in string?

def find_dup_char(input):
	x=[]
	for i in input:
		if i not in x and input.count(i)>1:
			x.append(i)
	print(" ".join(x))

if __name__ == "__main__":
	input = input("enter your word")
	find_dup_char(input)
