# Exercise 2: This program counts the distribution of the hour of the day for each of the messages. 
# You can pull the hour from the “From” line by finding the time string and then splitting that 
# string into parts using the colon character. Once you have accumulated the counts for each hour, 
# print out the counts, one per line, sorted by hour as shown below.

file_name = input("Enter file:")
if len(file_name) < 1 : file_name = "mbox-short.txt"
file_hand = open(file_name)

from_lst = list()
aux = list()
hour_lst = list()
for line in file_hand :
    if line.startswith("From ") :
        from_lst = line.split()
        aux = from_lst[5].split(":")
        hour_lst.append(aux[0])

hour_dict = dict()
for key in hour_lst :
    hour_dict[key] = hour_dict.get(key,0) + 1

for key, item in sorted(hour_dict.items()) :
    print(key, item)