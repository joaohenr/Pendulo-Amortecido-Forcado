import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
import math

rc('font',**{'family':'serif','serif':['Computer Modern Roman']}) #fonte para os graficos
rc('text', usetex=True)

def g(t,y,z,F,q,w):
    return -z/q -math.sin(y) + F*math.sin(w*t)                  #funcao do problema

def rungekutta(y0,z0,F,q,w):
    y, z, k1y, k1z, k2y, k2z, k3y, k3z, k4y, k4z = ([0 for i in range(N+1)] for i in range(10))
    t = np.arange(0,N+1,h).tolist()      #lista tempo com intervalo h                                                                       
    y[0] = y0                            #condicoes inicais
    z[0] = z0
    for i in range(N):
        k1y = h*z[i]                                                    
        k1z = h*g(t[i],y[i],z[i],F,q,w)                 #calculando os k           
        k2y = h*(z[i] + k1z/2)
        k2z = h*g(t[i] + h/2, y[i] + k1y/2, z[i] + k1z/2,F,q,w)
        k3y = h*(z[i] + k2z/2)
        k3z = h*g(t[i] + h/2, y[i] + k2y/2, z[i] + k2z/2,F,q,w)
        k4y = h*(z[i] + k3z)
        k4z = h*g(t[i] + h, y[i] + k3y, z[i] + k3z,F,q,w)
        y[i+1] = y[i] + (k1y + 2*k2y + 2*k3y + k4y)/6       #rungekutta para y
        z[i+1] = z[i] + (k1z + 2*k2z + 2*k3z + k4z)/6       #rungekutta para z
        if y[i+1] > math.pi:
            y[i+1] = y[i+1] - 2*math.pi #condicao para manter o valor de theta entre -pi e pi
        if y[i+1] < -math.pi:
            y[i+1] = y[i+1] + 2*math.pi
    return t,y,z


for F in [0.2, 0.9, 1.07, 1.20, 1.35, 1.45, 1.47, 1.5]:         #looping para cada forca
    h, N =0.01, 200000
    t,y,z=rungekutta(0,0,F,2,2/3)                               #runge-kutta 
    plt.plot(y[100000:],z[100000:],'darkblue',label='$F=%.2f$' %F,linewidth =0.7)#plot
    plt.grid(linestyle='dotted',color='black')
    plt.xlabel(r'$\theta$',fontsize=18)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.ylabel(r'$\dot{\theta}$',fontsize=18,rotation=0)
    plt.title('Espa\c{c}o de Fase',fontsize=20)
    plt.legend(fontsize=14)
    plt.savefig('espaco_fase_sem_transiente%.2f.png'%F)
    plt.show()

