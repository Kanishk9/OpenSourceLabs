def square(n):
    return n*n

list1 = [2,3,4,6]

list2 = list(map(square, list1))
print(list2)