import sys
import numpy as np

num = 5
num1 = np.int8(1)

print(type(num))
print(sys.getsizeof(num))

print(type(num1))
print(sys.getsizeof(np.int8))
