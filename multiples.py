# Multiples
# Part 1: create a program that prints all odd numbers from 1 to 1000
# use for loop and don't use array

for i in range (1, 1001):
    if i % 2 != 0:
        print i

# Part 2: create another program that prints all multiples of 5 from 5 to 10,000

for i in range (5, 10001):
    if i % 5 == 0:
        print i

# Sum List
# create a program that prints the sum of all values in a List

a = [1, 2, 5, 10, 255, 3]
sum = 0
for i in a:
    sum += i
print sum

# Average List
#create a program that prints the average of all values in a list

a = [1, 2, 5, 10, 255, 3]
sum = 0
for i in a:
    sum += i
avg = sum/len(a)
print avg

# Odd And Even
# create a function that counts from 1 to 2000. as it loops through each number, have your program generate the number and specify whether it is odd or even

def oddOrEven():
    for x in range (1, 2001):
        if x % 2 == 0:
            print x, "is an even number."
        else:
            print x,  "is an odd number."

# oddOrEven()

# create a function that reads each value in a list and returns a list where each value has been multipled by 5

def multiplyArr(arr, n):
    newArr = []
    for x in arr:
        newArr.append(x * n)
    return newArr

# print multiplyArr([1,2,3,4,5], 5)

# Scores And Grades
# create a program that prompts the user ten times for a test score between 60 and 100. each time a score is generated, your program should display what the grade is for a particular score. (A, B, C, D)

def scoresAndGrades():
    print "Scores and Grades"
    for x in range(0, 10):
        print "What is your score?"
        score = input()
        if score < 60:
            grade = "F"
            print "Your grade is", grade
        elif score >= 60 and score < 70:
            grade = "D"
            print "Your grade is", grade
        elif score >= 70 and score < 80:
            grade = "C"
            print "Your grade is", grade
        elif score >= 80 and score < 90:
            grade = "B"
            print "Your grade is", grade
        elif score >= 90 and score <= 100:
            grade = "A"
            print "Your grade is", grade
    print "End of the program Bye!"

# scoresAndGrades()

# Coin Toss
# create a program that simulates tossing a coin 5,000 times. program should display how many times the head/tail appears ("attempt #1: throwing a coin...its a head! got 1 head so far and 0 tails so far")

import random
def coinToss():
    total = 0
    heads = 0
    tails = 0
    for x in range (0, 10):
        rand = round(random.random())
        total += 1
        if rand == 0:
            heads += 1
            print "Attempt #{}: Flipping a coin...it's heads! Got {} head(s) so far and {} tail(s) so far.".format(total, heads, tails)
        elif rand == 1:
            tails +=1
            print "Attempt #{}: Flipping a coin...it's tails! Got {} head(s) so far and {} tail(s) so far.".format(total, heads, tails)
    print "Ending the program. Bye!"

# coinToss()

# Stars Assignment
# create a function called draw_stars() that takes a list of numbers and prints out * based on the value of the number in the list

def drawStars():
    a = [1,2,3,4,5,6,7,8,9,10]
    for x in a:
        print x * "*"

# drawStars()

# Part 2: modify the function to allow a list containing integers and strings. when a string is passed, instead of displaying *, display the first letter of the string as many times as are letters in the string

def drawStarsTwo():
    a = ["Preeya", 17, "Cassidy", 4, 10, "Hello", 0, "World"]
    for x in a:
        if type(x) is str:
            print x[0].lower() * len(x)
        else:
            print x * "*"

# drawStarsTwo()

# Tuples

t = ("a", "b", "c", "z", "s", "q", "d")
print max(t)
# max is alphanumerical if the data are strings

# Assignment: Dictionaries of Names

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

for dict in students:
    for key, data in dict.items():
        print data

# Part 2

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

#for each key value pair in users
for key, data in users.items():
    #print the key(students/instructors)
	print key.title()
	counter = 0
    #for each dictionary inside of data(the lists)
	for dic in data:
		counter = counter +1
        #each first and last name inside of each dictionary
		full_name = dic["first_name"] + " " + dic["last_name"]
		full_name_upper = full_name.upper()
		name_count = len(dic["first_name"]) + len(dic["last_name"])
		print counter, full_name_upper, name_count

# Bubble Sort

def bubbleSort(lst):
    swapped = True
    while swapped:
        swapped = False
        for x in range(len(lst) - 1):
            if lst[x] > lst[x+1]:
                print "swapping", lst[x]
                lst[x], lst[x+1] = lst[x+1], lst[x]
                swapped = True
    return lst

# print bubbleSort([2,4,1,6,5,7,3])

# create a list of 100 random values between 0 and 1000. implement a bubble sort that returns a sorted list

random_list = [random.randint(0, 1001) for count in range(100)]

# print bubbleSort(random_list)






















# selectionSort([1,2,3])
