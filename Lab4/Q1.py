import numpy as np

print("Enter elements of the list: ")
ini_array = np.array(input().split())

unique, frequency = np.unique(ini_array, return_counts=True)
for x, y in zip(unique, frequency):
    print("{} appeared {} times".format(x,y))