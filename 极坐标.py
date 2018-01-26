import matplotlib.pyplot as plt
import numpy as np

#r=np.arange(1,6)
r=np.empty(5)
r.fill(5)
theta=[0,np.pi/2,np.pi,3*np.pi/2,2*np.pi]
ax=plt.subplot(projection='polar')
ax.plot(theta,r,'r',linewidth=2)

