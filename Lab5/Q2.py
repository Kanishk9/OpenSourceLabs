import numpy as np
import matplotlib.pyplot as plt

Result1 = np.array([2,5,8,5])
Result2 = np.array([3,2,5,7])
method = np.array(['A','B','C','D'])
x1 = np.arange(len(Result1))
x2 = [x + 0.25 for x in x1]
plt.bar(x1, Result1, width=0.25, label='Result1')
plt.bar(x2, Result2, width=0.25, label='Result2')
plt.xticks([x + 0.1 for x in x1], method)
plt.legend()
plt.show()