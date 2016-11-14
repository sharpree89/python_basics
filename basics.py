# Getting User Input
greetings = "Hello Ninja!"
print greetings
print 'What is your name?'
name = raw_input()
print "How old are you?"
age = input()
print "Your name is", name
print "You are", age, "years old"
raw_input("\n\nPress the enter key to exit.")

# Strings
first = "preeya"
last = "Sharma"
full = "preeya SHARMA"
print "My name is {} {}".format(first, last)

# Upper and Lower Case
print first.capitalize()
print last.lower()
print full.swapcase()
print first.upper()
print full.lower()

# Substrings
my_string = "hello world"
print my_string.find("el")

# Replace part of a string
my_string = "hello world world world world"
print my_string.replace("world", "kitty")
# optional numerical parameter to indicate the max num of times to replace the word
print my_string.replace("world", "kitty", 3)

# Lists

# remove() removes the given VALUE
x = [1,2,3,3,3,3,4,5]
x.remove(3)
print x

# pop() removes the value at the given INDEX
y = [10,11,12,13,14]
y.pop(1)
print y

# slice()
x = [99,4,2,5,-3];
print x[:]
#the output would be [99,4,2,5,-3]
print x[1:]
#includes everything at index 1 and AFTER
#the output would be [4,2,5,-3];
print x[:4]
#includes everything up UNTIL index 4
#the output would be [99,4,2,5]
print x[2:4]
# includes index 2 and 3, but not 4
# the output would be [2,5];

# append() a value to an array
x = [5,34,10,1,6]
x.append(2)
x += [2]
print x

# print items on a separate line
names = ['KB', 'Oliver', 'Mikey', 'John', 'Michael']
print '\n'.join(names)
