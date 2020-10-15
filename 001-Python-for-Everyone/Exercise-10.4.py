# Exercise 4: Add code to the above program to figure out who has the most messages in the file. 
# After all the data has been read and the dictionary has been created, look through the dictionary 
# using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages 
# and print how many messages the person has.

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

flag = True
for key in email :
    while flag :
        maximun = email[key]
        flag = False
    if email[key] > maximun :
        maximun = email[key]
        name = key

print(name, maximun)
