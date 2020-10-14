# Exercise 1: Write a program to read through a file and print the contents of the file 
# (line by line) all in upper case. 

file_name = input("Enter a file name: ")
file_hand = open(file_name)

for line in file_hand :
    print(line.upper())
    