import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline
import mpl_toolkits.axisartist as axisartist

fig = plt.figure()
ax = axisartist.Subplot(fig, 111)
fig.add_axes(ax)
ax.axis["left"].set_axisline_style("->", size = 1)
ax.axis["bottom"].set_axisline_style("->", size = 1)
ax.axis["top"].set_visible(False)
ax.axis["right"].set_visible(False)

x=np.linspace(0,200,200)

y=list()

for i in range(len(x)):
    if(i<=10):
        y.append(0.00001)
    elif(i<=35):
        y.append(y[i-1]*1.2)
    elif(i<100):
        y.append(0.001)
    else:
        y.append(y[i-10]*0.5)


plt.ylim(0.000,0.0011)
plt.xlabel('Epoch')
plt.ylabel('Learning Rate')

plt.title('Dynamic Learning Rate')

# print(len(x),len(y))

plt.plot(x,y,color='red',label='Learning Rate')

# x_new=[0,35,100]
# y_new=[0.00001,0.001,0.001]

x_new=[0]
y_new=[0.00001]

for i in range(10,35,1):
    x_new.append(i)
    y_new.append(y_new[-1]*1.2)

x_new.extend([35,100])
y_new.extend([0.001,0.001])

for i in range(110,200,10):
    x_new.append(i)
    y_new.append(y_new[-1]*0.5)


plt.scatter(x_new,y_new,color='blue',marker='*')


plt.annotate('Warm Up', xy=(5,0.00001), xytext=(-15 ,100), textcoords='offset points',
             arrowprops=dict(arrowstyle='fancy', connectionstyle='arc3,rad=0.3'),
             bbox=dict(boxstyle='round,pad=0.5', fc='gray', ec='k', lw=1,alpha=0.5))

plt.annotate('Gradual WarmUp', xy=(30,0.0004), xytext=(30,-30), textcoords='offset points',
             arrowprops=dict(arrowstyle='simple', connectionstyle="angle3,angleA=80,angleB=50"),
             bbox=dict(boxstyle='round,pad=0.5', fc='gray', ec='k', lw=1,alpha=0.5))


plt.annotate('Multiplicative Decay', xy=(130,0.00012), xytext=(10,100), textcoords='offset points',
             arrowprops=dict(arrowstyle='wedge', connectionstyle="arc3,rad=0.3"),
             bbox=dict(boxstyle='round,pad=0.5', fc='gray', ec='k', lw=1,alpha=0.5))



plt.grid(linestyle='--', linewidth=1, color='gray', alpha=0.4)
plt.legend()
plt.show()