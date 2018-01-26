import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,10)
fig1=plt.figure()
ax=fig1.add_subplot(111)
plt.plot(x,x)
plt.plot(x,x*2)
plt.plot(x,x*3)
ax.legend(['normal','fast','faster'])


