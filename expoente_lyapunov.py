import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
import math
from scipy.optimize import curve_fit  #modulo scipy

rc('font',**{'family':'serif','serif':['Computer Modern Roman']})
rc('text', usetex=True)

def g(t,y,z,F,q,w):
    return -z/q -math.sin(y) + F*math.sin(w*t)

def rungekutta(y0,z0,F,q,w):
    y, z, k1y, k1z, k2y, k2z, k3y, k3z, k4y, k4z = ([0 for i in range(N+1)] for i in range(10))
    t = np.arange(0,N+1,h).tolist()
    y[0] = y0
    z[0] = z0
    for i in range(N):
        k1y = h*z[i]
        k1z = h*g(t[i],y[i],z[i],F,q,w)
        k2y = h*(z[i] + k1z/2)
        k2z = h*g(t[i] + h/2, y[i] + k1y/2, z[i] + k1z/2,F,q,w)
        k3y = h*(z[i] + k2z/2)
        k3z = h*g(t[i] + h/2, y[i] + k2y/2, z[i] + k2z/2,F,q,w)
        k4y = h*(z[i] + k3z)
        k4z = h*g(t[i] + h, y[i] + k3y, z[i] + k3z,F,q,w)
        y[i+1] = y[i] + (k1y + 2*k2y + 2*k3y + k4y)/6           # rungekutta para y
        z[i+1] = z[i] + (k1z + 2*k2z + 2*k3z + k4z)/6           # rungekutta para \
    
    return t,y,z        #nao temos mais a restricao de -pi a pi !!!!


q, w, h, N= 2, 2/3, 0.01, 200000
t,y,z=rungekutta(0,2,1.2,q,w)     #condicao inicial 0 e 2
theta1=y                            
t,y,z=rungekutta(0.001,2.001,1.2,q,w) #condicao inicial 0.0001 e 2.0001
theta2 = y                                  
theta=abs(np.array(theta2)-np.array(theta1)) #grandeza theta
t= np.array(t)                                  
T = 105000              #tempo 
def func(x, a, b, c):
    return a * np.exp(-b * x) + c    #funcao do ajuste

popt, pcov = curve_fit(func,t[0:T],theta[0:T])  #ajuste

#plot
plt.plot(t[0:T],func(t[0:T],*popt),'r--',label='ajuste: $a=%5.3f$, $|\lambda_{l}|=%5.3f$, $c=%5.3f$' % tuple(popt) )

t=t.tolist()                #t vira uma lista
theta=theta.tolist()        #theta vira uma lista

plt.plot(t[0:T],theta[0:T],color='teal',label='F=1.2',linewidth=2) #segundo plot
plt.grid(linestyle='dotted',color='black')
plt.xlabel(r'$t(s)$',fontsize=18)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.ylabel(r'$\Delta\theta$',fontsize=18,rotation=0)
plt.yscale('log')
plt.title("Expoente de Lyapunov",fontsize=20)
plt.legend(fontsize=14)
plt.savefig('expoente.pdf',dpi=300)
plt.show()

