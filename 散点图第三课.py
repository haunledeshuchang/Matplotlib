import numpy as np
import matplotlib.pyplot as plt
N=1000
X1=np.random.randn(N)
Y1=-X1+np.random.randn(N)*0.5
plt.scatter(X1,Y1)
plt.show()