import matplotlib.pyplot as plt
import numpy as np
x=np.arange(-10,11)
y=x*x
plt.plot(x,y)
plt.text(-2,40,'function:y=x*x',family='serif',style='italic')
plt.text(-2,20,'function:y=x*x',family='fantasy',style='oblique',bbox=dict(facecolor='r',alpha=0.2))
