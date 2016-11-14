# Ternary Operators
# <result_if_true> if <condition> else <result_if_false>

stacks = 2
print('Coding Dojo' if stacks == 3 else 'You are not Coding Dojo!')

stacks = 3
print('Coding Dojo' if stacks == 3 else 'You are not Coding Dojo!')

stacks = 4
print('Coding Dojo' if stacks == 3 else 'You are not Coding Dojo!')

# Lambda Functions are lightweight anonymous functions

def add1(num1, num2):
    return num1 + num2
print(add1(3,4))

# Can be rewritten as:

add2 = lambda num1, num2: num1 + num2
print(add2(3,4))

# quick way to iterate through a list:

result = map(lambda x: x**2, [1,2,4,99])
print(list(result))

# first parameter of map() is a function, second parameter is the actual arguement you want to pass into the function
