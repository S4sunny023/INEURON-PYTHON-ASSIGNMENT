#5.	Write a Python Program to Remove Punctuation From a String?

import string
def remove_punctuation(text):
    punctuations = set(string.punctuation)
    result = ''.join(char for char in text if char not in punctuations)

    return result


text = "Hello, World! This is a earth."

result = remove_punctuation(text)


print(result)
