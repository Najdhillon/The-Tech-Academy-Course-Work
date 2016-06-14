import sys, datetime, time
from math import pi

# Question one:

print('Twinkle,Twinkle, little star, \n\t How I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \n Twindle, twinkle, little star, \n\t How I wonder what you are \n')

#Question two:
print(sys.version)

#Question three:

unix = time.time()
date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))

print(date)

#Question 4:

r = float(input("Input of radius is: "))


area = str(pi * r ** 2)

print(area)

#Question 5:


firstname = input("What is your First Name: ")
lastname = input("What is your Last Name: ")

print(lastname + "\t" + firstname)

#Question 6:

values = input("Input values with comma : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)

#Question 7:


