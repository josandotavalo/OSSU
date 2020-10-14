# Exercise 6: Rewrite the program that prompts the user for a list of numbers and prints out the 
# maximum and minimum of the numbers at the end when the user enters “done”. Write the program to 
# store the numbers the user enters in a list and use the max() and min() functions to compute the 
# maximum and minimum numbers after the loop completes.

num_lst = list()

while True :
    number = input("Enter a number: ")
    if number == "done" :
        break
    num_lst.append(number)

max_num = max(num_lst)
min_num = min(num_lst)

print("Maximun: ", max_num)
print("Minimun: ", min_num)
