import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
import math
from scipy.optimize import curve_fit

rc('font',**{'family':'serif','serif':['Computer Modern Roman']})
rc('text', usetex=True)

def g(t,y,z,F,q,w):
    return -z/q -math.sin(y) + F*math.cos(w*t) 

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
        z[i+1] = z[i] + (k1z + 2*k2z + 2*k3z + k4z)/6           # rungekutta para y'
        if y[i+1] > math.pi:
            y[i+1] = y[i+1] - 2*math.pi
        if y[i+1] < -math.pi:
            y[i+1] = y[i+1] + 2*math.pi
    return t,y,z
#--------------------------------*--------------------------------*--------------------

#<<<<-----------------Mapa de poincaré---------------------
#for F in [0.2, 0.9, 1.07, 1.20, 1.35, 1.45, 1.47, 1.5]:
    #q, w, h, N = 2, 2/3, 0.01,100000
    #t,y,z=rungekutta(0,0,F,q,w) # evolui o sistem para um estado sem transiente
    #a = []
    #b = []
    #for i in range(10000):
        #h = 0.01*2*math.pi/w
        #N = 100                             # anda 1 periodo
        #t,y,z=rungekutta(y[-1],z[-1],F,q,w)
        #a.append(y[-1])
        #b.append(z[-1])
    
    #plt.scatter(a,b,label='$F=%.2f$' %F,color='purple',s=0.3)
    #plt.grid(linestyle='dotted',color='black')
    #plt.xlabel(r'$\theta$',fontsize=18)
    #plt.xticks(fontsize=14)
    #plt.yticks(fontsize=14)
    #plt.ylabel(r'$\dot{\theta}$',fontsize=18,rotation=0)
    #plt.title("Mapa de Poincare",fontsize=20)
    #plt.legend(fontsize=14)
    #plt.savefig('mapa_de_poincare%.2f.pdf'%F.dpi=300)
    #plt.show()
#

#--------------------Diagrama de Bifurcação------------

#Forca = np.arange(1.35,1.5,0.0001).tolist()
#for F in Forca:
    #f=[]
    #a=[]
    #q, w, h, N = 2, 2/3, 0.01,100000
    #t,y,z=rungekutta(0,0,F,q,w) # evolui o sistem para um estado sem transiente
    #for i in range(1000):
        #h = 0.01*2*math.pi/w
        #N = 100                             # anda 1 periodo
        #t,y,z=rungekutta(y[-1],z[-1],F,q,w)
        #a.append(y[-1])
        #f.append(F)
        
    #plt.scatter(f,a,color='purple',s=1)

#plt.grid(linestyle='dotted',color='black')
#plt.xlabel(r'$F$',fontsize=18)
#plt.xticks(fontsize=14)
#plt.yticks(fontsize=14)
#plt.ylabel(r'$\theta$',fontsize=18,rotation=0)
#plt.title("Diagrama de Bifurca\c{c}\~{a}o",fontsize=20)
#plt.savefig('diagrama_bifurcacao.png')
#plt.show()
#-------------------Expoente de lyapunov--------------------------
#q, w, h, N= 2, 2/3, 0.01, 200000
#t,y,z=rungekutta(0,2,1.2,q,w)
#theta1=y
#t,y,z=rungekutta(0.001,2.001,1.2,q,w)
#theta2 = y
#theta=abs(np.array(theta2)-np.array(theta1))
#t= np.array(t)
#T = 105000
#def func(x, a, b, c):
    #return a * np.exp(-b * x) + c

#popt, pcov = curve_fit(func,t[0:T],theta[0:T])


#plt.plot(t[0:T],func(t[0:T],*popt),'r--',label='ajuste: $a=%5.3f$, $|\lambda_{l}|=%5.3f$, $c=%5.3f$' % tuple(popt) )

#t=t.tolist()
#theta=theta.tolist()

#plt.plot(t[0:T],theta[0:T],color='teal',label='F=1.2',linewidth=2)
#plt.grid(linestyle='dotted',color='black')
#plt.xlabel(r'$t(s)$',fontsize=18)
#plt.xticks(fontsize=14)
#plt.yticks(fontsize=14)
#plt.ylabel(r'$\Delta\theta$',fontsize=18,rotation=0)
#plt.yscale('log')
#plt.title("Expoente de Lyapunov",fontsize=20)
#plt.legend(fontsize=14)
#plt.savefig('expoente.pdf',dpi=300)
#plt.show()




#--------------------Energia do osilaçor-----------------------
#for F in [0,0.1,0.2,0.5, 1.2,1.45,1.47, 1.5]:
    #q, w, h, N = 10, 2/3, 0.01,100000
    #t,y,z=rungekutta(-0.5,1,F,q,w)
    #z=(np.array(z)**2)/2
    #y = 1-np.cos(np.array(y))
    #E = z + y
    #t= np.array(t)
    #if F==0:
        #def func(x, a, b, c):
            #return a * np.exp(-b * x) + c
        #popt, pcov = curve_fit(func,t[0:10000],E[0:10000])
        #plt.plot(t[0:10000],func(t[0:10000],*popt),'b--',label='ajuste: $a=%5.3f$, $\gamma=%5.3f$, $c=%5.3f$' % tuple(popt) )
        #pass

    #t = t.tolist()
    #E = E.tolist()
    
    #plt.plot(t[0:10000],E[0:10000],label='$F=%.2f$' %F,color='indianred',linewidth =2)
    #plt.grid(linestyle='dotted',color='black')
    #plt.xlabel(r'$t$(s)',fontsize=18)
    #plt.xticks(fontsize=14)
    #plt.yticks(fontsize=14)
    #plt.ylabel(r"$E'$ (dimes\~{a}o apropriada)",fontsize=18)
    #plt.title("Energia do Oscilador",fontsize=20)
    #plt.legend(fontsize=14)
    #plt.savefig('energia_oscilador%.2f.pdf'%F,dpi=300)
    #plt.show()


#--------------------------------------------------------------------**
#q, w, h, N = 4, 2/3, 0.01,209000
#t,y,z=rungekutta(0,0,1.5,q,w) # evolui o sistem para um estado sem transiente

#z0=z[-1]
#y0=y[-1]
#-------sensibilidade as condições iniciais------------
#t,y,z=rungekutta(1,-1,1.5,4,2/3)
#plt.plot(y[0:940],z[0:940],label='$F=0.2$')
#t,y,z=rungekutta(1.1,-1.1,1.5,4,2/3)
#plt.plot(y[0:940],z[0:940])
##-----------------------------------

#------movimento dissipativo-------
#h,N = 0.01,200000
#t,y,z=rungekutta(-1,1,0,4,2/3)
#plt.plot(y,z,'darkblue',label='$F=0$')
#plt.plot(t[0:10000],z[0:10000],'purple')
#plt.grid(linestyle='dotted',color='black')
#plt.xlabel(r'$\theta$',fontsize=18)
#plt.xticks(fontsize=14)
#plt.ylabel(r'$\dot{\theta}$',fontsize=18,rotation=0)
#plt.yticks(fontsize=14)
#plt.title('Espa\c{c}o de Fase Amortecido',fontsize=20)
#plt.legend(fontsize=14)
#plt.savefig('espaco_fase_amortecido.pdf')
#plt.show()

#---------------------------
#---------------movimento caotico--- Espaço de fase-------------
#for F in [0.2, 0.9, 1.07, 1.20, 1.35, 1.45, 1.47, 1.5]:
    #h, N =0.01, 200000
    #t,y,z=rungekutta(0,0,F,2,2/3)
    #plt.plot(y[100000:],z[100000:],'darkblue',label='$F=%.2f$' %F,linewidth =0.7)
    #plt.grid(linestyle='dotted',color='black')
    #plt.xlabel(r'$\theta$',fontsize=18)
    #plt.xticks(fontsize=14)
    #plt.yticks(fontsize=14)
    #plt.ylabel(r'$\dot{\theta}$',fontsize=18,rotation=0)
    #plt.title('Espa\c{c}o de Fase',fontsize=20)
    #plt.legend(fontsize=14)
    #plt.savefig('espaco_fase_sem_transiente%.2f.png'%F)
    #plt.show()


#plt.grid(linestyle='dotted',color='black')
#plt.xlabel(r'$\theta(t)$',fontsize=18)
#plt.ylabel(r'$\dot{\theta}(t)$',fontsize=18)
#plt.title('Espa\c{c}o de F\~{a}se sem Transiente',fontsize=14)
#plt.legend(fontsize=12)
#plt.savefig('espaco_fase_c.png')
#plt.show()
