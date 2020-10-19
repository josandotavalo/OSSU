# Exercise 1: Write a simple program to simulate the operation of the grep command on
# Unix. Ask the user to enter a regular expression and count the number of lines that 
# matched the regular expression:

import re

reg_expression = input("Enter a regular expression: ")
file_name = "mbox.txt"
file_hand = open(file_name)

count = 0
for line in file_hand :
	if re.search(reg_expression, line) :
		count = count + 1

print("mbox had ", count, "lines that matched ", reg_expression)
