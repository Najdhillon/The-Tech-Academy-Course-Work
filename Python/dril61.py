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

filename = input('Please name the file: ')
fext = filename.split(".")
print('The extension is ' + fext[1])


#Question 8:

color_list =['Red','Green','White', 'Black']

print('The first color is ' + color_list[0])
print('The last color is ' + color_list[3])


#Question 9:
examdate = (11,12,2014)

print('The examination will start from: %i/%i/%i'%examdate)

#Question 10:

a = 5
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)

#Question 11:
print(abs.__doc__)

#Question 12:

import calendar

m = int(input('What month is it?'))
y = int(input('What year is it?'))

print(calendar.month(y,m))


#Question 13:

print(""" 
a string that you "don't" have to escape 
This 
is a  ....... multi-line 
heredoc string --------> example 
""")

#Question 14

from datetime import date  
  
date1 = date(2014, 7, 2)  
date2 = date(2014, 7, 11)  
delta = date1 - date2  
print(delta.days)

#Question 15:
from math import pi

radius = int(input('What is the radius? '))
print(radius)


volume = float(4.0/3.0) * pi * (radius*radius*radius)
print(volume)


#Question 16:

num1 = int(input("Please input a number"))



if num1 > 17:

    print((num1 - 17)*2)
    
else:

    print(17-num1)

#Question 17:
    
def near_thousand(n):  
      return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))  


print(near_thousand(1000))

#Question18:

def someFun():

    x = int(input('Input a value: '))
    y = int(input('Input a value: '))
    z = int(input('Input a value: '))

    total = x + y + x

    if x == y == z:

        total = total * 3
        print(total)


someFun()

#Question 19:



        
def someFun19():

    xstr = input('Share some words: ')

    if len(xstr) >= 2 and xstr[:2] == "Is":
        print(xstr)
    print("Is " + xstr) 


someFun19()

        
# Question 20:

def larger_string(str, n):
   result = ""
   for i in range(n):
      result = result + str
   return result

print(larger_string('yo', 5))


# 21:

num = int(input("Please provide a even or odd number: "))

check = num % 2
if check > 0:
    print('odd number')

else:

    print('even number')


#22:

def list_count_4(nums):
  count = 0  
  for num in nums:
    if num == 4:
      count = count + 1

  return count

print(list_count_4([1, 4, 8, 7, 4]))
print(list_count_4([4, 4, 4, 4, 4, 4]))






