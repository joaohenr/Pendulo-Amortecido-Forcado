import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
import math
from scipy.optimize import curve_fit


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
        z[i+1] = z[i] + (k1z + 2*k2z + 2*k3z + k4z)/6           # rungekutta para z
        if y[i+1] > math.pi:
            y[i+1] = y[i+1] - 2*math.pi
        if y[i+1] < -math.pi:
            y[i+1] = y[i+1] + 2*math.pi
    return t,y,z

for F in [0,0.1,0.2,0.5, 1.2,1.35,1.45,1.47]: #looping forca
    q, w, h, N = 10, 2/3, 0.01,100000
    t,y,z=rungekutta(-0.5,1,F,q,w)      #runge-kutta ara condicao inicial -0.5 e 1
    z=(np.array(z)**2)/2                #energia cinetica
    y = 1-np.cos(np.array(y))           #energia potencial
    E = z + y                           #energia total
    t= np.array(t)
    if F==0:                        
        def func(x, a, b, c):       #ajusta apenas para F = 0
            return a * np.exp(-b * x) + c
        popt, pcov = curve_fit(func,t[0:10000],E[0:10000])
        plt.plot(t[0:10000],func(t[0:10000],*popt),'b--',label='ajuste: $a=%5.3f$, $\gamma=%5.3f$, $c=%5.3f$' % tuple(popt) )
        pass

    t = t.tolist()
    E = E.tolist()
                                                        #segundo plot
    plt.plot(t[0:10000],E[0:10000],label='$F=%.2f$' %F,color='indianred',linewidth =2)
    plt.grid(linestyle='dotted',color='black')
    plt.xlabel(r'$t$(s)',fontsize=18)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.ylabel(r"$E'$ (dimens\~{a}o apropriada)",fontsize=18)
    plt.title("Energia do Oscilador",fontsize=20)
    plt.legend(fontsize=14)
    plt.savefig('energia_oscilador%.2f.pdf'%F,dpi=300)
    plt.show()

