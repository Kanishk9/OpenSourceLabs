import scipy.linalg as la
import numpy as np

x = np.array([[5,4], [6,3]])

x, y = la.eig(x)
print(x)
print("")
print(y)