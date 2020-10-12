# Exercise 5: Write a program which prompts the user for a Celsius temperature, 
# convert the temperature to Fahrenheit, and print out the converted temperature.

str_celsius = input("Enter Celsius temperature: ")
float_celsius = float(str_celsius)
float_fahrenheit = 32 + (float_celsius * (9/5))
print("Fahrenheit temperature: ", float_fahrenheit)