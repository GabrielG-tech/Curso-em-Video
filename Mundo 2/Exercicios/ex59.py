import os
import sys
os.system('cls' if os.name == 'nt' else 'clear')
print('{:=^40}'.format(' DESAFIO 59 '))
print('Digite dois valores para operação.')
n1 = float(input('Digite o 1º Número: '))
n2 = float(input('Digite o 2º Número: '))
print('''
[1] somar
[2] multiplicar
[3] maior valor
[4] novos números
[5] sair do programa''')
resposta = int(input('Digite sua escolha: '))
while resposta != 5:
    if resposta == 1:
        print(n1, '+', n2, '=', n1 + n2)
    if resposta == 2:
        print(n1, 'x', n2, '=', n1 * n2)
    if resposta == 3:
        print(max(n1, n2))
    if resposta == 4:
        resposta = int(input('Digite sua escolha: '))
