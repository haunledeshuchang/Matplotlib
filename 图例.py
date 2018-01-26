import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,10)
plt.plot(x,x)
plt.plot(x,x*2)
plt.plot(x,x*3)
plt.legend(['normal','fast','faster'],loc=0,ncol=3)
plt.gca()
plt.locator_params('x',nbins=5)


