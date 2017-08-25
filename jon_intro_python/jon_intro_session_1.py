# Jon intro to python; session 1; 8/23/17:

## variables:



# integers:

num1 = 1

print(num1)

type(num1)


# strings:

string1 = 'a string'

string2 = '1'


num2 = 3

num1 + num2

output = num1/num2

type(output)



# create new variable from operation (float):



# type(num3)



# boolean variables and operators
result = num1 < num2


#
# num2 >= num1

type(result)


# operators:

# <, >, >=, <=, !=, in, not in, modulo (%)

# modulo example:

5%2





# lists (creating, appending, indexing):


# create a list:
our_list = [1,2,3,4,5]


# determine list length (i.e. how many items are in the list):

len(our_list)


our_list.append(7)


# mixed lists:
our_second_list = [1,2,3,4,5, 'number', 'another string', [7,8,9]]



# indexing into a list:

len(our_second_list)

our_second_list[-2][2]



# appending to a list (list.append()):

our_second_list.append('rachel')





# removing from a list (list.pop())
output = our_second_list.pop()


#
print('our output is:', output)






# dictionary:

# create dictionary:
dict = {}




# append to dictionary (dict['key] = value):


dict['kyle'] = [3129522848, 23]
dict['jackie'] = 3129545568
dict['jon'] = 3129523468


dict['kyle'][1]



# make a dictionary:







# importing modules (ex: from math import sqrt):


from math import sqrt


sqrt(16)







## functions!


# basic addition function:

# def addition_calc(number1,number2):
#     return number1 + number2



def addition_calc(num1, num2):
    return num1 + num2


addition_calc(1,6)




# let's build a pythagorean theorem calculator:

# pythagorean theorem = a^2 + b^2 = c^2


def pyth_theorem(a,b):
    c = sqrt(a**2+b**2)
    return c
    #print(c)


output = pyth_theorem(2,3)


# for loops:


# let's create a list, and print out each item:


list1 = ['kyle','rachel','joe','bruce']

for u in list1:
    print(u)



num_list = [16, 25, 9, 23, 76]

num_list2 = [16, 9, 99]


for item in num_list:
    if item in num_list2:
        print('item also in list 2:', item)

