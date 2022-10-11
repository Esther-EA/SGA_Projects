import numpy as np

# Generate an array of numbers between 1 and 100 with both numbers included and find the LCM of the even numbers. 
arr = np.arange(1, 101, 2)
x = np.lcm.reduce(arr)
print(x)