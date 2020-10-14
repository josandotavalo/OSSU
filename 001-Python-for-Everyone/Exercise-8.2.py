# Exercise 2: Write a program to prompt for a file name, and then read through the file and look for 
# lines of the form:
# X-DSPAM-Confidence: 0.8475
# When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract 
# the floating-point number on the line. Count these lines and then compute the total of the spam 
# confidence values from these lines. When you reach the end of the file, print out the average 
# spam confidence.

def extract_number(text) :
    posicition = text.find(":")
    num = text[posicition + 1 : len(text)]
    f_num = float(num)
    return f_num

total = 0
count = 0

# Use the file name mbox-short.txt as the file name
file_name = input("Enter a file name: ")
file_hand = open(file_name)
for line in file_hand :
    if not line.startswith("X-DSPAM-Confidence:") : continue
    number = extract_number(line)
    total = total + number
    count = count + 1

print("Done")
print("Average spam confidence:", total/count)