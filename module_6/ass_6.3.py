import numpy as np
arr = np.arange(1, 101, 2)
x = np.lcm.reduce(arr)
print(x)