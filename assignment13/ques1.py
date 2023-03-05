'''Question 1:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated
sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24'''

import math


C = 50
H = 30


input_str = input("Enter comma-separated sequence of values for D: ")
input_list = input_str.split(",")


Q_list = []


for D_str in input_list:
  
    D = float(D_str)

    
    Q = math.sqrt((2 * C * D) / H)

   
    Q_list.append(str(round(Q))) 


output_str = ",".join(Q_list)
print(output_str)
