import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,10)
y1=x*x
y2=np.log(x)
fig=plt.figure()
ax1=fig.add_subplot(111)
ax1.plot(x,y1)
ax1.set_ylabel('Y1')
ax2=ax1.twinx()
ax2.plot(x,y2,'r')
ax2.set_ylabel('Y2')
ax1.set_xlabel('Compare Y1 and Y2')
