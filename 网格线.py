import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,10)
fig1=plt.figure()
ax1=fig1.add_subplot(111)
plt.plot(x,x)
ax1.grid(color='g')

