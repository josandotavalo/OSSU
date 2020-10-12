# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate 
# for hours worked above 40 hours.

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
if h > 40 :
    pay = h*r + (h-40.0)*0.5*r
else :
	pay = h*r
print(pay)