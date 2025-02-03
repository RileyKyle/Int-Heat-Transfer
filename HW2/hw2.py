#%%
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

from numpy import pi, sin, sinh
#%% problem 2

def theta_F(x,y,a,b,T0,itr=20000):
    theta = 0
    for n in range(1,itr+1):
        Cn = (2/n/pi)*(1-(-1)**n)*T0/sinh(n*pi*b/a)*1.0
        theta += Cn*sin(n*pi*x/a)*np.nan_to_num(sinh(n*pi*y/a))
    return theta/T0

a = 1
b = 1.5*a
n = 100
small_num = 0#1E-250

xini = np.linspace(small_num,a-small_num,n)
yini = np.linspace(small_num,b-small_num,n)
x,y = np.meshgrid(xini,yini)
theta = theta_F(x,y,a=a,b=b,T0=100)

contours = plt.contour(x,y,theta,levels=[0.001,0.01,0.05,0.1,0.2,0.4,0.6,0.8,0.9])
plt.colorbar()
plt.clabel(contours, inline = False, fontsize=12, colors = 'k')
plt.show()