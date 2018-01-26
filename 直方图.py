import numpy as np
import matplotlib.pyplot as plt
mu=100
sigma=20
x1=mu+sigma*np.random.randn(200000)
plt.hist(x1,bins=100,normed=True)
#plt.hist(x1,bins=100)
plt.show

