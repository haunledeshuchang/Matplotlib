import matplotlib.pyplot as plt
import numpy as np
x=np.arange(-10,11)
y=x*x
plt.plot(x,y)
plt.annotate('this is the bottom',xy=(0,0),xytext=(0,20),arrowprops=dict(facecolor='r',headwidth=20,width=10))

