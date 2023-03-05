'''Question 3:
Write a program that accepts a comma separated sequence of words as input and prints the
words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:'''

words = input("Enter comma-separated words: ")

# Split the input string into a list of words
word_list = words.split(",")

# Sort the list of words alphabetically
sorted_list = sorted(word_list)

# Join the sorted list of words back into a string, separated by commas
result = ",".join(sorted_list)

# Print the result
print(result)
