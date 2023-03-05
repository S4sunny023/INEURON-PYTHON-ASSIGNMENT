'''Question 2:
Write a program to compute the frequency of the words from the input. The output
should output after sorting the key alphanumerically.
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or
Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1

'''

sentence = input("Enter a sentence: ")


freq_dict = {}


words = sentence.split()


for word in words:
    if word in freq_dict:
        freq_dict[word] += 1
    else:
        freq_dict[word] = 1


sorted_dict = {k: v for k, v in sorted(freq_dict.items(), key=lambda item: item[0])}


for key, value in sorted_dict.items():
    print(key + ":" + str(value))
