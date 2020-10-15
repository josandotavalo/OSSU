# Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to 
# count how many messages have come from each email address, and print the dictionary.

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

print(email)