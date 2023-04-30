#4.	Write a Python Program to Sort Words in Alphabetic Order?


# function to sort words in alphabetical order
def sort_words(words):
    words_list = words.split()
    words_list.sort()
    result = ' '.join(words_list)
    return result

words = "i am doing project in ineuron"


result = sort_words(words)
print(result)
