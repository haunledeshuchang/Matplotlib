import matplotlib.pyplot as plt
import numpy as np
x1=np.arange(0,10)
y1=np.random.rand(len(x1))
fig=plt.figure()
ax=fig.add_subplot(111)
plt.plot(x1,y1)
ax.set_title('object oriented')
plt.show()

