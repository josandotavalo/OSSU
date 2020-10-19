import re

file_name = "Actual-data.txt"
file_hand = open(file_name)

add = 0
for line in file_hand :
	print(line)
	number = re.findall('[0-9]+',line)
	for item in number :
		add = add + int(item)
print(add)