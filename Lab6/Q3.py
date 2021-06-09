from scipy import linalg
import numpy as np

a = np.array([[4,5], 
              [3,2]])

x = linalg.det(a)
y = linalg.inv(a)

print(x)
print("")
print(y)