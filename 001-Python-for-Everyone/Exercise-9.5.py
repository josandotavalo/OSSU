# Exercise 5: Write a program to read through the mail box data and when you find line that starts 
# with “From”, you will split the line into words using the split function. We are interested in who 
# sent the message, which is the second word on the From line.
# You will parse the From line and print out the second word for each From line, then you will also 
# count the number of From (not From:) lines and print out a count at the end. 

file_name = input("Enter file name: ")
if len(file_name) < 1 : file_name = "mbox-short.txt"

file_hand = open(file_name)
count = 0

for line in file_hand :
    if line.startswith("From:") :
        aux = line.split()
        email = aux[1]
        print(email)
        count = count + 1

print("There were", count, "lines in the file with From as the first word")