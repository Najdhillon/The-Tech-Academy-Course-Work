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


#Question 23:

def substring_copy(str, n):
  check = 2
  if check > len(str):
    check = len(str)
  substr = str[:check]
  
  result = ""
  for i in range(n):
    result = result + substr
  return result


print(substring_copy('abcdef', 2))
print(substring_copy('p', 3));

#Question 24:

def is_vowel(char):
    vowels = 'aeiou'
    return char in vowels
           

print(is_vowel('u'))

#Question 25:

def valuecheck(groupv, n):

    for val in groupv:

        if n == val:
            return True
        
    return False

print(valuecheck([1,2,3,4,5],6))

#Question 26:

def histogram( items ):
    for n in items:
        output = ''
        times = n
        while( times > 0 ):
          output += '*'
          times = times - 1
        print(output)

histogram([2, 3, 6, 5])

#Question 27:

def connectstuff(list):

    finish = ''

    for parts in list:

        finish += str(finish)
    return finish

print(connectstuff([1, ' pig', 2, ' pig']))

#Question 28:

numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

for x in numbers:

    if x == 248:

        break

    elif x % 2 == 0:

        print(x)

#Question 29:

color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])

print(color_list_1.difference(color_list_2))


#Question 30:

def findarea():

    a = int(input('Input base: '))
    b = int(input('Input height: '))

    area = ((a * b)/2)
    print(area)

findarea()

#Question 31:

from fractions import gcd

print(gcd(20,8))

#question 32:

from fractions import gcd

def lcm(a,b):

    return a * b // gcd(a,b)

print(lcm(20,8))

#Question 33:

def sumThree(a,b,c):

    if a == b or b == c or c == a:

        total = 0

    else:

        total = a + b + c
        return total

print(sumThree(3,3,3))

print(sumThree(3,5,4))


#Question 34:

def sumTwo(a,b):
    
    total = a + b

    if total in range(15,20):

        return 20

    else:
        
        return total

print(sumTwo(5,10))

print(sumTwo(16,10))


#Question 35:

def sumdif(a,b):
    
    if a == 5 or b or b == 5 or abs(a-b) == 5 or (a+b) == 5:

        return True

    else:
        
        return False

print(sumdif(2,2))

print(sumdif(16,10))




#Question 36:


def add_num(a, b):  
    if not (isinstance(a, int) and isinstance(b, int)):  
         raise TypeError("Inputs must be integers")  
    return a + b  
  
print(add_num(1, 2))

print(add_num('test', 2))

# Question 37:

def pdetail():

    name = 'Name'
    age = '12'
    addr = 'Merica'

    print("Name: {} \nAge: {} \nAddress: {}".format(name,age, addr))


pdetail()

#Question 38:

def q38(x,y):

    eq = ((x+y) ** 2)
    print(eq)


q38(5,5)


#Question 39:

amt = 10000  
int = 3.5  
years = 7  
  
future_value  = amt*((1+(0.01*int)) ** years)  
print(future_value)  


#Question 40:

import math

p1 = (1,3)

p2 = (2,4)

distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

print(distance)


#Question 41:

import os

open('test.txt', 'w')

print(os.path.isfile('test.txt'))


#Question 42:

import struct
print(struct.calcsize("P") * 8)

#Question 43:

import platform
import os
print(os.name)
print(platform.system())
print(platform.release())


#Question 44:

import site; 
print(site.getsitepackages())

#Question 45:

from subprocess import call
call(["ls", "-l"])

#Question 46:

import os
print(os.path.realpath(__file__))


#Question 47:

import multiprocessing
print(multiprocessing.cpu_count())

#Question 48:

n = "1.2"
print(float(n))
print(int(float(n)))

#Question 49:

from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('/Users/Naj/Documents/The-Tech-Academy-Course-Work') if isfile(join('/Users/Naj/Documents/The-Tech-Academy-Course-Work', f))]
print(files_list);


#Question 50:

for i in range(0,10):

    print('.', end="")

#Question 51:

import cProfile
def sum():
    print(1+0)
cProfile.run('sum()')

#Question 52:

from __future__ import print_function
import sys

def eprint(*args, **kwargs):

    print(*args, file=sys.stderr, **kwargs)


eprint("tes", "test", "est", sep="---")

          
#Question 53:

import os

print(os.environ['HOME'])


#Question 54:

import getpass
print(getpass.getuser())

#Question 55:

import socket

print(socket.gethostbyname(socket.gethostname()))

#Question 56:

import shutil

print(shutil.get_terminal_size())


