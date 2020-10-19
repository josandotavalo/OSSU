# Exercise 2: Write a program to look for lines of the form:
# New Revision: 39772
# Extract the number from each of the lines using a regular expression and the findall() 
# method. Compute the average of the numbers and print out the average as an integer.

import re

file_name = "mbox-short.txt"
file_hand = open(file_name)

add = 0
count = 0
for line in file_hand :
	if re.search('^New Revision', line) :
		number = re.findall('[0-9]+',line)
		for item in number :
			add = add + int(item)
			count = count + 1
print(add/count)