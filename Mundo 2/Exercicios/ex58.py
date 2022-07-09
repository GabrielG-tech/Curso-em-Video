print('{:=^40}'.format(' DESAFIO 58 '))
import random
numero_aleatorio = random.randint(0, 10)
tentativa = int(input('Tente adivnha o número que estou pensando [0-10]: '))
while tentativa != numero_aleatorio:
    tentativa = int(input('Ops! Você errou... Tente novamente: '))
print(f'Parabens você acertou!\nEra {numero_aleatorio} mesmo!')
