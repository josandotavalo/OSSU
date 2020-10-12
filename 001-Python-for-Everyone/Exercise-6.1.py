# Exercise 1: Write a program which repeatedly reads numbers until the user enters “done”. 
# Once “done” is entered, print out the total, count, and average of the numbers. 
# If the user enters anything other than a number, detect their mistake using try and except 
# and print an error message and skip to the next number.

suma = 0
count = 0

while True:
    number = input("Enter a number: ")
    if number == "done":
        print(suma, count, suma/count)
        break
    try :
        num = int(number)
        suma = suma + num
        count = count + 1
    except :
        print("Invalid input")
        continue