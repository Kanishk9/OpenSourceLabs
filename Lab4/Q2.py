import numpy as np

arr = np.array(list(input("Enter binary no: ")))
arr = np.sort(arr)[::-1]
result = ""
for i in arr:
    result += i
print(result)