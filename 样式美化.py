import matplotlib.pyplot as plt
import numpy as np
#plt.style.use('ggplot')
plt.style.use('fivethirtyeight')
fig,axes=plt.subplots(ncols=2,nrows=2)
ax1,ax2,ax3,ax4=axes.ravel()
x,y=np.random.normal(size=(2,100))
ax1.plot(x,y,'o')

x=np.arange(0,10)
y=np.arange(0,10)
ncolors=len(plt.rcParams['axes.prop_cycle'])
shift=np.linspace(0,10,ncolors)
for s in shift:
    ax2.plot(x,y+s,'-')


x=np.arange(5)
y1,y2,y3=np.random.randint(1,25,size=(3,5))
width=0.25
ax3.bar(x,y1,width)
ax3.bar(x+width,y2,width,color=plt.rcParams['axes.prop_cycle'].by_key()['color'][1])
ax3.bar(x+2*width,y3,width,color=plt.rcParams['axes.prop_cycle'].by_key()['color'][2])

for i, color in enumerate(plt.rcParams['axes.prop_cycle']):
    xy=np.random.normal(size=3)
    ax4.add_patch(plt.Circle(xy,radius=0.2))#这里有问题，需要注意课程中的源代码
ax4.axis('equal')




