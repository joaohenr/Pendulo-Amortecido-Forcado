import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
import math
import rungekutta
rc('font',**{'family':'serif','serif':['Computer Modern Roman']})
rc('text', usetex=True)


Forca = np.arange(1.35,1.5,0.0005)
f = []
a = []
for F in Forca:
    q, w, N = 2, 2/3,200000
    h = 0.01*2*np.pi/w
    t,y,z=rungekutta.rungekutta(N,h,0,0,F,q,w) # evolui o sistem para um estado sem transiente
    #h = 0.001*2*np.pi/w
    #N = 1000                     # anda um periodo
    for i in range(100):
        N = 1000
        h = 0.001*2*np.pi/w
        t,y,z=rungekutta.rungekutta(N,h,y[-1],z[-1],F,q,w) #evolui o sistema 1 perido
        a.append(y[-1])
        f.append(F)
        

plt.scatter(f,a,color='purple',s=3)
plt.ylim([1,3])
plt.grid(linestyle='dotted',color='black')
plt.xlabel(r'$F$',fontsize=18)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.ylabel(r'$\theta$',fontsize=18,rotation=0)
plt.title("Diagrama de Bifurca\c{c}\~{a}o",fontsize=20)
plt.savefig('img/diagrama_bifurcacao/diagrama_bifurcacao.png',dpi=300)
plt.savefig('img/diagrama_bifurcacao/diagrama_bifurcacao.pdf',dpi=300)

plt.show()

