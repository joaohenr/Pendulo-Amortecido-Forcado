import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
import rungekutta

rc('font',**{'family':'serif','serif':['Computer Modern Roman']})
rc('text', usetex=True)



for F in [0.2, 0.9, 1.07, 1.20, 1.35, 1.45, 1.47, 1.5]:#looping forca
    q, w, h, N = 2, 2/3, 0.01,100000
    t,y,z=rungekutta.rungekutta(N,h,0,0,F,q,w)  #evolui o sistema para um estado sem transiente
    a = []                      #lista muda
    b = []                      #lista muda
    for i in range(10000):
        h = 0.01*2*np.pi/w
        N = 100                             #anda 1 periodo do elemento forcador
        t,y,z=rungekutta.rungekutta(N,h,y[-1],z[-1],F,q,w)
        a.append(y[-1])                    #adicionamos o ultimo elementos na lista a 
        b.append(z[-1])                    #adicionamos o ultimo elementos na lista b 

    plt.scatter(a,b,label='$F=%.2f$' %F,color='purple',s=0.3)#plot
    plt.grid(linestyle='dotted',color='black')
    plt.xlabel(r'$\theta$',fontsize=18)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.ylabel(r'$\dot{\theta}$',fontsize=18,rotation=0)
    plt.title("Mapa de Poincare",fontsize=20)
    plt.legend(fontsize=14)
    plt.savefig('img/mapa_poincare/mapa_de_poincare%.2f.png'%F,dpi=300)
    plt.show()

