# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a 
# function called computepay which takes two parameters (hours and rate).

def computepay(hours, rate):
    if h > 40 :
        pay = h*r + (h-40.0)*0.5*r
    else :
	    pay = h*r   
    print("Pay: ",pay)

hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
try :
    h = float(hrs)
    r = float(rate)
    computepay(h,r)
except :
    print("Error, please enter numeric input")