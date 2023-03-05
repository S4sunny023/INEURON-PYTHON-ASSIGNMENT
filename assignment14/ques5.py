'''Question 5:
Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".
'''

import zlib


original_string = b"hello world!hello world!hello world!hello world!"
compressed_string = zlib.compress(original_string)


decompressed_string = zlib.decompress(compressed_string)


print("Original string:", original_string)
print("Compressed string:", compressed_string)
print("Decompressed string:", decompressed_string)
