# Exercise 2: Write a program that categorizes each mail message by which day of the week the commit 
# was done. To do this look for lines that start with “From”, then look for the third word and keep a 
# running count of each of the days of the week. At the end of the program print out the contents of 
# your dictionary (order does not matter).

file_name = input("Enter the file name: ")
file_hand = open(file_name)

aux = list()
keys = list()
days = dict()

for line in file_hand :
    if line.startswith("From ") :
        aux = line.split()
        keys.append(aux[2])

for key in keys :
    days[key] = days.get(key,0) + 1

print(days)
        