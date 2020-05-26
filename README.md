# Pendulo-Amortecido-Forcado
Estudo sobre um pêndulo com atrito viscoso e com uma força periódica.
## Pré-requisitos
* [python](https://www.python.org/)
* [numpy](https://numpy.org/)
* [matplotlib](https://matplotlib.org/)
* [scipy](https://www.scipy.org/)
* [LaTeX 2e](https://www.latex-project.org/)
## Arquivos

* ```rungekutta.py``` : resolve a equação do pêndulo via método rungekutta e retornando os vetores tempo, posição e velocidade.
* ```diagrama_bifurcacao.py``` : plota o diagrama de bifurcação. 
* ```energia_oscilador.py``` : plota a energia do pêndulo para cada valor de força.
* ```espaco_fase.py``` : plota o espaço de fase para cada valor de força.
* ```mapa_poincare.py``` : plota o mapa de poincaré para cada força. F = 1.2 e F = 1.5 regime caótico.
* ```expoente_lyapunov.py``` : calcula o expoente de lyapunov.
* ```relatorio.pdf```: relatório do estudo.

Todos os arquivos, menos o ```expoente_lyapunov.py```, precisam do arquivo rungekutta.py.

