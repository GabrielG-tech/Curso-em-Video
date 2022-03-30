print('='*14 + ' DESAFIO 51 ' + '='*14)
print(' '*10, '10 Temos de uma P.A.')
print('='*40)
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
décimo = n + (10 - 1) * r
for c in range(n, décimo + r, r):
    print(c, end=' → ')
print('Fim')
