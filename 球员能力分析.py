import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
font=FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=10)
plt.style.use('ggplot')
ax1=plt.subplot(221,projection='polar')
ax2=plt.subplot(222,projection='polar')
ax3=plt.subplot(223,projection='polar')
ax4=plt.subplot(224,projection='polar')
ability_size=6
ability_label=['进攻','防守','盘带','速度','体力','射术']
player={
    'M':np.random.randint(size=ability_size,low=70,high=99),
    'H':np.random.randint(size=ability_size,low=70,high=99),
    'P':np.random.randint(size=ability_size,low=70,high=99),
    'Q':np.random.randint(size=ability_size,low=70,high=99),
}
theta=np.linspace(0,2*np.pi,6,endpoint=False)#如果没有endpoint=False，则该等差数列的最后一个值包含在theta取值中，则下面theta又增加了一个值，将会导致theta的取值太多
theta=np.append(theta,theta[0])

player['M']=np.append(player['M'],player['M'][0])
ax1.plot(theta,player['M'],'r')
ax1.fill(theta,player['M'],'r',alpha=0.5)
ax1.set_xticks(theta)
ax1.set_xticklabels(ability_label,y=-0.02,fontproperties=font,color='r')#y值表示ability_label距离极坐标图的距离，越大越近
ax1.set_title('梅西',position=(0.5,1.01),fontproperties=font,color='r',fontsize=15)

player['H']=np.append(player['H'],player['H'][0])
ax2.plot(theta,player['H'],'g')
ax2.fill(theta,player['H'],'g',alpha=0.5)
ax2.set_xticks(theta)
ax2.set_xticklabels(ability_label,y=-0.02,fontproperties=font,color='g')#y值表示ability_label距离极坐标图的距离，越大越近
ax2.set_title('哈维',position=(0.5,1.01),fontproperties=font,color='g',fontsize=15)

player['P']=np.append(player['P'],player['P'][0])
ax3.plot(theta,player['P'],'b')
ax3.fill(theta,player['P'],'b',alpha=0.5)
ax3.set_xticks(theta)
ax3.set_xticklabels(ability_label,y=-0.02,fontproperties=font,color='b')#y值表示ability_label距离极坐标图的距离，越大越近
ax3.set_title('皮克',position=(0.5,1.01),fontproperties=font,color='b',fontsize=15)

player['Q']=np.append(player['Q'],player['Q'][0])
ax4.plot(theta,player['Q'],'y')
ax4.fill(theta,player['Q'],'y',alpha=0.5)
ax4.set_xticks(theta)
ax4.set_xticklabels(ability_label,y=-0.02,fontproperties=font,color='y')#y值表示ability_label距离极坐标图的距离，越大越近
ax4.set_title('切赫',position=(0.5,1.01),fontproperties=font,color='y',fontsize=15)
