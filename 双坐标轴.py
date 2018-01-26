import matplotlib.pyplot as plt
import numpy as np
x=np.arange(2,20)
y1=x*x
y2=np.log(x)
plt.plot(x,y1)
plt.twinx()
plt.plot(x,y2,color='r')

