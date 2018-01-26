import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon#这是新知识需要注意

def func(x):
    return -(x-2)*(x-8)+40
x=np.linspace(0,10)
y=func(x)

fig,ax=plt.subplots()
plt.plot(x,y,'r',linewidth=2)
a=2
b=9
ax.set_xticks([a,b])
ax.set_yticks([])
ax.set_xticklabels([r'$a$',r'$b$'])
plt.figtext(0.9,0.05,'$x$')
plt.figtext(0.09,0.9,'$y$')
ax.set_ylim(ymin=25)#调整y的最小值
ix=np.linspace(a,b)
iy=func(ix)
ixy=zip(ix,iy)
verts=[(a,0)]+list(ixy)+[(b,0)]
poly=Polygon(verts,facecolor='0.8',edgecolor='0.2')
ax.add_patch(poly)

plt.text(0.5*(a+b),35,r'$\int^b_a(-(x-2)*(x-8)+40)dx$',horizontalalignment='center',fontsize=20)
