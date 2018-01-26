import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

fig=plt.subplot()
plt.grid()
xy1=np.array([0.2,0.2])
xy2=np.array([0.2,0.8])
xy3=np.array([0.8,0.2])
xy4=np.array([0.8,0.8])
circle=mpatches.Circle(xy1,0.2)
fig.add_patch(circle)
rectangle=mpatches.Rectangle(xy2,0.2,0.1,color='r')
fig.add_patch(rectangle)
polygon=mpatches.RegularPolygon(xy3,5,0.1,color='g')
fig.add_patch(polygon)
ellipse=mpatches.Ellipse(xy4,0.2,0.1,color='y')
fig.add_patch(ellipse)
plt.axis('equal')
