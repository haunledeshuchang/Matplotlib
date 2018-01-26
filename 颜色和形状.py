import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,5)
plt.plot(y,color='g',marker='o',linestyle='--')
plt.plot(y+1,color='0.5',marker='D',linestyle='-.')
plt.plot(y+2,color='#FF00FF',marker='^',linestyle=':')
plt.plot(y+3,color=(0.1,0.2,0.3),marker='P',linestyle='-')

