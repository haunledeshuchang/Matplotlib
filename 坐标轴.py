import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import datetime
fig=plt.figure()
start=datetime.datetime(2015,1,1)
end=datetime.datetime(2016,1,1)
delta=datetime.timedelta(days=1)
dates=mpl.dates.drange(start,end,delta)
y=np.random.rand(len(dates))
ax=plt.gca()
plt.plot_date(dates,y,linestyle='--')
date_format=mpl.dates.DateFormatter('%y-%m-%d')
ax.xaxis.set_major_formatter(date_format)
fig.autofmt_xdate()





