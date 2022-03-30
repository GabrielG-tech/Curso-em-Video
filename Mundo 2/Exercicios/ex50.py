print('='*12 + ' DESAFIO 50 ' + '='*12)
soma = 0
cont = 0
for c in range(0, 6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += num
        cont += 1
    print('Soma de todos os pares até agora: {}'.format(soma))
print('Dos {} números pares que você informou, a soma é {}.'.format(cont, soma))
