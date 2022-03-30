print('{:=^40}'.format(' DESAFIO 55 '))
pesox = 0
maior = 0
menor = 0
for c in range(0, 3):
    peso = float(input('Digite seu peso: '))
    if peso > pesox:
        maior = peso
    if peso < pesox:
        menor = peso
    peso = pesox
print('O maior peso é {} e o menor é {}.'.format(maior, menor))
