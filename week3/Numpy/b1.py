import numpy as np 
a = np.random.randint(0, 10, 10)
print(a)
print([i for i in a if (i < 8 and i > 3)])
