print('='*14 + ' DESAFIO 55 ' + '='*14)
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é \033[1m{}Kg\033[m e o menor é \033[1m{}Kg\033[m.'.format(maior, menor))
