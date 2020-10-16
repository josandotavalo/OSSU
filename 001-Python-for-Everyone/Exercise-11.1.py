# Exercise 1: Revise a previous program as follows: Read and parse the “From” lines and pull out the 
# addresses from the line. Count the number of messages from each person using a dictionary.
# After all the data has been read, print the person with the most commits by creating a list of 
# (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the 
# person who has the most commits.

file_name = input("Enter the file name: ")
file_hand = open(file_name)

aux = list()
keys = list()
email = dict()

for line in file_hand :
    if line.startswith("From ") :
        aux = line.split()
        keys.append(aux[1])

for key in keys :
    email[key] = email.get(key,0) + 1

max_email = 0
max_commit = 0
flag = True

for key,item in email.items() :
    while flag :
        max_commit = item
        flag = False
    if item > max_commit :
        max_email = key
        max_commit = item

print(max_email, max_commit)

