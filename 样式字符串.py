import matplotlib.pyplot as plt
import numpy as np
data=np.arange(1,5)
y=np.arange(1,5)
plt.plot(y,'cx--')
plt.plot(y+1,'kp:')
plt.plot(y+2,'mo-.')
plt.show()
