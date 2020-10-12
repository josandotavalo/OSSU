# Exercise 2: Rewrite your pay program using try and except so that your program handles 
# non-numeric input gracefully by printing a message and exiting the program. 
# The following shows two executions of the program:

hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
try :
    h = float(hrs)
    r = float(rate)
    if h > 40 :
        pay = h*r + (h-40.0)*0.5*r
    else :
	    pay = h*r   
    print(pay)
except :
    print("Error, please enter numeric input")