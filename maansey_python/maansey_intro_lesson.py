# intro to python:

# variables:


# initializing integers:
num1 = 23


# initializing strings:
#string1 = 'a string'

# initializing floats:

#float1 = float(5)


# operators (<, >, <=, ==, !=, in, not in):

# boolean data types:

#num2 = 67

#result = num1 > num2

#num2 >= num1









# lists (creating, appending, indexing, pop):



#our_list = []

#our_second_list = [1,3,5,7,'string1','string2']

#len(our_second_list)


#our_second_list.append('')

#output = our_second_list.pop()

# example of print function:

#print 'our output is:', output


#our_second_list




# dictionary data structure:

#dict = {}

#dict['kyle'] = 3129522848

#dict['rachel'] = 3127465867

#dict['joe'] = 3124567645










# importing modules (ex: from math import sqrt):


from math import sqrt


#sqrt(16)



# creating functions:

# functions (ex: calculate side of triangle using pyth. theorem; build a tip calculator):


#def addition_calc(number1,number2):
#    return number1 + number2

from math import sqrt

import math

sqrt(16)

2**3

def nameOfFun(x):
    print x


nameOfFun('print statement')








#result = addition_calc(1,2)

#printer_func('this is a string')


# let's build a pythagorean theorem calculator:

#a = 7

#a**2


# pyth theorem = a^2 + b^2 = c^2







def pythagoras(a,b):
    c = sqrt(a**2+b**2)
    print 'length of c:', c


pythagoras(2,4)




















# for loops:



#list1 = ['kyle','rachel','joe','bruce']

#list1.append('vanessa')

for each_item in list1:
    print each_item

#num_list = [16, 25, 9, 23, 76, 99]

#num_list2 = [16, 9, 99]

for each_num in num_list:
    if each_num in num_list2:
        print 'number is in other list:', each_num
    else:
        print 'number is not in the other list', each_num





# fizz buzz: loop through list of integers, and if number is even, pring 'fizz',
# if number is odd, print 'buzz'

# hint: modulo operator ('%')

















for num in num_list:
    if num%2 == 0:
        print num, 'fizz'
    elif num%2 == 1:
        print num, 'buzz'

































def tip_calculator(meal_cost, tax_rate, tip_percent):
    tax_amount = meal_cost*(tax_rate/float(100))
    tip_amount = (meal_cost+tax_amount)*(tip_percent/float(100))
    meal_total = meal_cost+tax_amount+tip_amount
    print 'meal total:', meal_total






meal_cost = 15
tax_rate = 6
tip_percent = 20

float(6/100)

tip_calculator(15,6,20)

list = ['a','b',3.14,'6',7]

list.append('x')
