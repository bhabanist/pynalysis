# This is a programming to use shooting method to solve an equation
'''
y" = -y + (2y'^2)/y
'''
import numpy as np
from scipy.integrate import odeint
zero = 10**(-5)
def f(u,x):
    y,z=u
    f1,f2 =z,-y +2*z**2/y
    return [f1,f2]

x = np.linspace(-1,1,100)
y0 = 1/(np.e + 1/np.e)
z1,z2 = 0.2,0.3

u=[y0,z1]
sol =odeint(f,u,x)
w1=sol[:,0][-1]
for i in range(50):
    u =[y0,z2]
    sol = odeint(f,u,x)
    w2 =sol[:,0][-1]

    if abs(w1-w2) < zero:
        break
    z1, z2 =z2, z2+ (z2-z1)*(y0-w2)/(w2-w1)
    w1=w2
import matplotlib.pyplot as plt

plt.plot(x,sol[:,0]-1/(np.exp(x)+np.exp(-x)), 'o', color='r')
#plt.plot(x, 1/(np.exp(x)+np.exp(-x)), 's',color ='b')
plt.show()