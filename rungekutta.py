#import matplotlib.pyplot as plt
#from matplotlib import rc
import numpy as np
import math

def g(t,y,z,F,q,w):
    return -z/q -math.sin(y) + F*math.sin(w*t)                  #funcao do problema

def rungekutta(N,h,y0,z0,F,q,w):
    y, z, k1y, k1z, k2y, k2z, k3y, k3z, k4y, k4z = ([0 for i in range(N+1)] for i in range(10))
    #y, z, k1y, k1z, k2y, k2z, k3y, k3z, k4y, k4z =np.zeros((10,N+1))
    t = np.arange(0,N+1,h)       #lista tempo com intervalo h                                                                       
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

