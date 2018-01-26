import  matplotlib.pyplot as plt
import numpy as np
N=5
x1=np.arange(N)
x2=np.arange(5,30,5)
x3=np.arange(2,17,3)
# bar_height=0.3
bar_width=0.3
# plt.bar(x1,x2,bar_height,color='b')
# plt.bar(x1,x3+bar_height,bar_height,color='r')
plt.bar(x1,x2,color='b')
plt.bar(x1,x3,color='r',bottom=x2)

plt.grid()

plt.show()