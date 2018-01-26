import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')
plt.figure(1,figsize=(8,8))
margin_border=0.1
width=0.6
margin_beween=0.03
height=0.2

left_s=margin_border
bottom_s=margin_border
width_s=width
height_s=width

left_x=margin_border
bottom_x=margin_border+width+margin_beween
width_x=width
height_x=height


left_y=margin_border+width+margin_beween
bottom_y=margin_border
width_y=height
height_y=width

rect_s=[left_s,bottom_s,width_s,height_s]
rect_x=[left_x,bottom_x,width_x,height_x]
rect_y=[left_y,bottom_y,width_y,height_y]

x=np.random.randn(500)
y=x+np.random.randn(500)*0.5


axScatter=plt.axes(rect_s)
axHisX=plt.axes(rect_x)
axHisY=plt.axes(rect_y)

axHisX.set_xticks([]) #取掉axHisX图的X坐标
axHisY.set_yticks([])#取掉axHisY图的Y坐标

axScatter.scatter(x,y,color='b')

binwidth = 0.25
xymax = max(np.max(np.abs(x)), np.max(np.abs(y)))
lim = (int(xymax/binwidth) + 1) * binwidth

axScatter.set_xlim((-lim, lim))
axScatter.set_ylim((-lim, lim))

bins = np.arange(-lim, lim + binwidth, binwidth)

axHisX.hist(x,bins=bins)
axHisY.hist(y,bins=bins,orientation='horizontal')