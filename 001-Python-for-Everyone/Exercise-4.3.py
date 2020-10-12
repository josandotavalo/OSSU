# Write a program to prompt for a score between 0.0 and 1.0. 
# If the score is out of range, print an error message. 
# If the score is between 0.0 and 1.0, print a grade.

score = input("Enter Score: ")
s = float(score)
if s < 0.0:
    print("Out of range")
elif s < 0.6:
    print("F")
elif s < 0.7:
    print("D")
elif s < 0.8:
    print("C")
elif s < 0.9:
    print("B")
elif s < 1.0:
    print("A")
else:
    print("Out of range")