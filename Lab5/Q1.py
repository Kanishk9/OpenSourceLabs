import numpy as np
import matplotlib.pyplot as plt

pi = np.pi
x = np.array([-pi, -pi/4, -pi/2, 0, pi/4, pi/2, pi])
tan, cot, sec, cosec = np.tan(x), 1/np.tan(x), 1/np.cos(x), 1/np.sin(x)
plt.plot(x, tan, label = 'Tan(x)')
plt.plot(x, cot, label = 'Cot(x)')
plt.legend()
plt.show()
plt.plot(x, sec, label = 'Sec(x)')
plt.plot(x, cosec, label = 'Cosec(x)')
plt.legend()
plt.show()