# Exercise 7: Rewrite the grade program from the previous chapter using a function called 
# computegrade that takes a score as its parameter and returns a grade as a string.

def computegrade(score) :
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

score = input("Enter Score: ")
s = float(score)
computegrade(s)
