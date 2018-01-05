import matplotlib.pyplot as plt
# import numpy as np
labes='A','B','C','D'
#A=np.arange(1,5)
A=[5,10,15,20]
plt.axes(aspect=1)

#plt.pie(x=A,labels=labes,autopct='%.2f')
plt.pie(x=A,labels=labes,autopct='%.1f%%')




