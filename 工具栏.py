import matplotlib.pyplot as plt
import numpy as np
N=1000
x=np.random.rand(N)
y=np.random.rand(N)
colors=np.random.rand(N)
#area=np.pi*(np.random.rand(N)*100)
area=np.random.rand(N)*100
plt.scatter(x,y,c=colors,alpha=0.5,s=area)