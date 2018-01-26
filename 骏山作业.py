# _*_ coding:utf-8 _*_
import numpy as np
import matplotlib.pyplot as plt
Time,Diameter=np.loadtxt('173.csv',delimiter=',',skiprows=1,usecols=(0,1),unpack=True)

plt.scatter(Time,Diameter,c='r',alpha=0.5)
plt.show()