def insertVal(i, list, val):
    for index in range(0, len(list)):
        if index == i:
            list.insert(i, val)
            return list
        elif i >= len(list):
            return False

print(insertVal(2, [1,2,4], 3))
