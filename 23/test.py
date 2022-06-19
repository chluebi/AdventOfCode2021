import numpy as np

i = 4
j = 4
for k in range(i, j, np.sign(j-i)):
    print(k)