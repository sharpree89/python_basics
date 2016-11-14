class Underscore(object):

    def map(self, arr, func):
        result = []
        for x in arr:
            result.append(func(x))
        return result

    def reduce(self, arr, func, result):
        for x in arr:
            result = func(x, result)
        return result

    def find(self, arr, func):
        for x in arr:
            if func(x):
                return x
        return "undefined"

    def filter(self, arr, func):
        result = []
        for x in arr:
            if func(x):
                result.append(x)
        return result

    def reject(self, arr, func):
        result = []
        for x in arr:
            if not func(x):
                result.append(x)
        return result

u = Underscore()

# Filters a list based on matching a specified condition
lambdaFilter = u.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print lambdaFilter

# Iterates through a list and carries out an operation to each item in the list
lambdaMap = u.map([1,2,3,4,5,6], lambda x: x * 10)
print lambdaMap
# print(list(lambdaMap))

# Finds the first item in a list that matches a given value
lambdaFind = u.find([1,2,3,4,5,6], lambda x: x == 3)
print lambdaFind

# Reduces a list down to one value based on given operation
lambdaReduce = u.reduce(["a", "b", "c"], (lambda x, y: x + y), "")
print lambdaReduce

# Filters a list based on NOT matching a specified condition
lambdaReject = u.reject([1,2,3,4,5,6], lambda x: x % 2 == 0)
print lambdaReject
