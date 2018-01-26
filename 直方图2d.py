import numpy as np
import matplotlib.pyplot as plt
x1=np.random.randn(1000)+2
x2=np.random.randn(1000)+3
plt.hist2d(x1,x2,bins=40)

