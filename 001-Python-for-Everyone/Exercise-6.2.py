# Exercise 2: Write another program that prompts for a list of numbers as above and at the end 
# prints out both the maximum and minimum of the numbers instead of the average.

largest = None
smallest = None
flag = True

while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try :
        number = int(num)
        while flag :
            largest = number
            smallest = number
            flag = False
        if number > largest :
            largest = number
        if number < smallest :
            smallest = number
    except :
        print("Invalid input")
        continue

print("Maximum is", largest)
print("Minimun is", smallest)