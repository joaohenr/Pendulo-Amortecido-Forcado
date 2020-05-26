import matplotlib.pyplot as plt
from matplotlib import rc
import rungekutta
rc('font',**{'family':'serif','serif':['Computer Modern Roman']})
rc('text', usetex=True)



for F in [0.2, 0.9, 1.07, 1.20, 1.35, 1.45, 1.47, 1.5]:
    h, N = 0.01, 200000
    t,y,z = rungekutta.rungekutta(N,h,0,0,F,2,2/3)              #chamo rungekutta para cada força, sem transiente
    plt.plot(y[100000:],z[100000:],'darkblue',label='$F=%.2f$' %F,linewidth =0.7)
    plt.grid(linestyle='dotted',color='black')
    plt.xlabel(r'$\theta$',fontsize=18)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.ylabel(r'$\dot{\theta}$',fontsize=18,rotation=0)
    plt.title('Espa\c{c}o de Fase',fontsize=20)
    plt.legend(fontsize=14)
    plt.savefig('img/espaco_fase/espaco_fase_sem_transiente%.2f.png'%F,dpi=00)
    plt.show()

