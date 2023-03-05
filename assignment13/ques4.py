'''
Question 4:
Write a program that accepts a sequence of whitespace separated words as input and prints
the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world'''

words = input("Enter whitespace-separated words: ")

# Split the input string into a list of words
word_list = words.split()

# Remove duplicate words from the list
unique_words = list(set(word_list))

# Sort the list of unique words alphanumerically
sorted_list = sorted(unique_words)

# Join the sorted list of unique words back into a string, separated by spaces
result = " ".join(sorted_list)

# Print the result
print(result)
