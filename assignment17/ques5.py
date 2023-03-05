'''
Question 5
Hamming distance is the number of characters that differ between two strings.
To illustrate:
String1: "abcbba"
String2: "abcbda"

Hamming Distance: 1 - "b" vs. "d" is the only difference.
Create a function that computes the hamming distance between two strings.
Examples
hamming_distance("abcde", "bcdef") ➞ 5

hamming_distance("abcde", "abcde") ➞ 0

hamming_distance("strong", "strung") ➞ 1
'''

def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        return None
    return sum(ch1 != ch2 for ch1, ch2 in zip(str1, str2))

print(hamming_distance("abcde", "bcdef"))

print(hamming_distance("abcde", "abcde")) 

print(hamming_distance("strong", "strung")) 


