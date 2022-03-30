print('='*14 + ' DESAFIO 52 ' + '='*14)
n = int(input('Número para análise: '))
tot = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[1;34m', end='')
        tot += 1
    else:
        print('\033[0;31m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisivel {} vezes.'.format(n, tot))
if tot == 2:
    print('Por isso ele \033[1mé\033[m primo.')
else:
    print('Por isso ele \033[1mnão é\033[m primo.')