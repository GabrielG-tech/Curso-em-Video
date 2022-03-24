print('='*12 + ' DESAFIO 50 ' + '='*12)
s = 0
for c in range(0, 6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        s += num
    print('Soma de todos os pares até agora: {}'.format(s))
print('A soma de todos os números pares digitados é {}.'.format(s))
