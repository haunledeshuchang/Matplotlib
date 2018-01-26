import matplotlib.pyplot as plt
import numpy as np
np.random.seed(1000)
data=np.random.normal(size=(1000,4),loc=0,scale=1)
labels=('A','B','C','D')
plt.boxplot(data,whis=0.5)
plt.show()

