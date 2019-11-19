import numpy as np
X = np.random.random((5,5))
MEAN = np.mean(X)
STD = np.std(X)

Z = (X-MEAN)/STD
print(Z)
np.save('X_normalized', Z)