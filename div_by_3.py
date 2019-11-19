import numpy as np

X = np.arange(1,101).reshape(10,10)
Y = X**2
Z = Y[Y%3==0]
print(Y)
print(Z)
np.save('div_by_3', Z)