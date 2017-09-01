# homework following intro to python session 1 (8/23/17)

# 1:

# write a function called 'tip_calculator' that accepts
# three arguments (meal_cost, tax_rate, tip_percent)
# and prints out the total cost of a meal including
# tax and tip;


def tip_calculator(meal_cost, tax_rate, tip_percent):
    tax_amount = meal_cost*(tax_rate/float(100))
    tip_amount = (meal_cost+tax_amount)*(tip_percent/float(100))
    meal_total = meal_cost+tax_amount+tip_amount
    print('meal total:', meal_total)


meal_cost = 15
tax_rate = 6
tip_percent = 20


tip_calculator(meal_cost,tax_rate,tip_percent)



# bonus: what if you wanted to improve the function
# by calculating how much each person in a group owed
# for the meal after adding tax and tip?

def group_tip_calculator(meal_cost, tax_rate, tip_percent,num_friends = 1):
    tax_amount = meal_cost*(tax_rate/float(100))
    tip_amount = (meal_cost+tax_amount)*(tip_percent/float(100))
    meal_total = meal_cost+tax_amount+tip_amount
    print('meal total:', meal_total/num_friends)

num_friends = 3

group_tip_calculator(meal_cost,tax_rate,tip_percent,num_friends) # NB default value of 1
# results in same function as above, but allows input to divide among how many friends
# you have (if you have any friends)


# 2:

# write a function that reverses the input (a list,
# provided below):

# list to reverse:
reverse_input = [6, 4, 'a_string', 3, 'another_string', 1.01, True]

# here we cheat and use built in functions (simple, efficient):
list(reversed(reverse_input))

# function method:

def reverser(input_list):
    output = []
    for i in range(1,len(input_list)+1):
        output.append(input_list[-i])
    return output

reverser(reverse_input)

# 3:

# using an imported python module, generate a list of
# 100 random integers between 0 and 1000 and save it to a variable

from random import randrange, randint, random

random_list = [randrange(1, 1000) for _ in range(0, 100)]


# 4:

# 4 A: what is the mean of this list?

sum(random_list)/len(random_list)

# alternative using numpy:

import numpy

numpy.mean(random_list)

# 4 B: what is the second highest value in this list?

set(random_list) # set removes duplicates, and orders the list

sorted(set(random_list))[-2]


# 5:

# write a function that counts how many even and
# odd numbers there are in a list; use this function
# to determine the number of evens and odds in the
# randomly generated list you just made

def e_and_o_counter(list):
    evens = 0
    odds = 0
    for i in list:
        if i%2 == 0:
            evens += 1
        elif i%2 == 1:
            odds += 1
    # return evens, odds
    print('number of evens:', evens, '\n','number of odds:', odds)

e_and_o_counter(random_list)


# 6: dictionaries

# class_roster is a dictionary containing 8th and 9th grade student
# information, including student IDs (8th grader's start w/ '8',
#  9th grader's start w/ '9') and grades on three exams

class_roster = {'ava': {'student_ID': '9113', 'test_scores': [94, 89, 95]},
 'jessica': {'student_ID': '9588', 'test_scores': [89, 95, 97]},
 'kendrick': {'student_ID': '8724', 'test_scores': [93, 91, 97]},
 'kyle': {'student_ID': '9988', 'test_scores': [85, 94, 92]},
 'morty': {'student_ID': '8776', 'test_scores': [74, 83, 81]},
 'rick': {'student_ID': '8423', 'test_scores': [99, 93, 94]},
 'titus': {'student_ID': '9441', 'test_scores': [88, 84, 85]},
 'veronica': {'student_ID': '8724', 'test_scores': [97, 95, 95]}}

# 6. A:

# update the class roster (programmatically) with the following students:


students_to_add = [['laura', 9111, [96, 93, 97]], ['stephanie', 9622, [93, 94, 97]], ['jared', 8954, [95, 91, 95]]]

students_to_add[0][0] # name
str(students_to_add[0][1])
students_to_add[0][2]

len(class_roster)

for i in students_to_add:
    class_roster[i[0]] = {'student_ID': str(i[1]), 'test_scores': i[2]}

class_roster['stephanie']['test_scores']
class_roster['rick']['test_scores']

# 6. B:

# create a list of all 8th grade student names:

eighth_graders = []

for key in class_roster:
    if class_roster[key]['student_ID'][0] == '8':
        eighth_graders.append(key)


# 6. C:

# add a new key/value pair for each student that represents their
# final grade (average of their 3 exam scores)

class_roster['stephanie']
sum(class_roster['stephanie']['test_scores'])
len(class_roster['stephanie']['test_scores'])

blah = sum(class_roster['stephanie']['test_scores'])/len(class_roster['stephanie']['test_scores'])

round(blah,2)

for key in class_roster:
    final_grade = sum(class_roster[key]['test_scores'])/len(class_roster[key]['test_scores'])
    class_roster[key]['final_grade'] = round(final_grade,2)


# 6. D:

# what is the class average for 8th graders? 9th graders?


blah = sum(class_roster['stephanie']['test_scores'])/len(class_roster['stephanie']['test_scores'])
blah2 = sum(class_roster['titus']['test_scores'])/len(class_roster['titus']['test_scores'])

(blah+blah2)/2 # 90.1666

v_scores = class_roster['stephanie']['test_scores']
t_scores = class_roster['titus']['test_scores']

sum(v_scores+t_scores)/len(v_scores+t_scores) # 90.1666

grades_8 = []
grades_9 = []


for key in class_roster:
    if class_roster[key]['student_ID'][0] == '8':
        grades_8.append(sum(class_roster[key]['test_scores'])/len(class_roster[key]['test_scores']))
    elif class_roster[key]['student_ID'][0] == '9':
        grades_9.append(sum(class_roster[key]['test_scores'])/len(class_roster[key]['test_scores']))


print('eighth grade average:',sum(grades_8)/len(grades_8))
print('ninth grade average:',sum(grades_9)/len(grades_9))