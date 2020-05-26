import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
from scipy.optimize import curve_fit
import rungekutta

rc('font',**{'family':'serif','serif':['Computer Modern Roman']})
rc('text', usetex=True)


for F in [0,0.1,0.2,0.5, 1.2,1.35,1.45,1.47]: #looping forca
    q, w, h, N = 10, 2/3, 0.01,100000
    t,y,z=rungekutta.rungekutta(N,h,-0.5,1,F,q,w)      #runge-kutta ara condicao inicial -0.5 e 1
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

                                                        #segundo plot
    plt.plot(t[0:10000],E[0:10000],label='$F=%.2f$' %F,color='indianred',linewidth =2)
    plt.grid(linestyle='dotted',color='black')
    plt.xlabel(r'$t$(s)',fontsize=18)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.ylabel(r"$E'$ (dimens\~{a}o apropriada)",fontsize=18)
    plt.title("Energia do Oscilador",fontsize=20)
    plt.legend(fontsize=14)
    plt.savefig('img/energia_oscilador/energia_oscilador%.2f.pdf'%F,dpi=300)
    plt.show()

