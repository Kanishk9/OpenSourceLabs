def giveOdd(n):
    if n%2!=0:
        return True
    else:
        return False

list1 = [2,3,6,7,11,15,22]

list2 = list(filter(giveOdd, list1))

print(list2)