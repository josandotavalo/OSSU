# Exercise 5: This program records the domain name (instead of the address) where the message was 
# sent from instead of who the mail came from (i.e., the whole email address). At the end of the 
# program, print out the contents of your dictionary.

file_name = input("Enter the file name: ")
file_hand = open(file_name)

aux = list()
domain = list()
email = dict()

for line in file_hand :
    if line.startswith("From ") :
        aux = line.split()
        keys = aux[1]
        aux_domain = keys.split("@")
        domain.append(aux_domain[1])

for key in domain :
    email[key] = email.get(key,0) + 1

print(email)