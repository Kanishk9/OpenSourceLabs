import numpy as np
from scipy import io as sio
arr = np.ones((4, 4))
sio.savemat('test.text', {'x': arr}) 
data = sio.loadmat('test.text' )
print(data['x'])
