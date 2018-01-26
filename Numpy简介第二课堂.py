import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def convert_date(date_bytes):
    return mdates.strpdate2num('%m/%d/%Y')(date_bytes.decode('ascii'))
date, open, close = np.loadtxt('000001.csv',delimiter=',',
                               converters={0: convert_date},
                               skiprows=1, usecols=(0,1,4), unpack=True)
# date,open,close=np.loadtxt('000001.csv',delimiter=',',converters={0:mdates.strpdate2num('%m/%d/%Y')},skiprows=1,usecols=(0,1,4),unpack=True)

plt.plot(date,open)


