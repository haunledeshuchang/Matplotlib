import numpy as np
import matplotlib.pyplot as plt
N=5
x1=np.arange(N)
x2=np.arange(5,30,5)
x3=np.arange(2,17,3)
bar_width=0.2
plt.bar(x1,x2,bar_width,color='b')
plt.bar(x1+bar_width,x3,bar_width,color='r')
plt.show()






