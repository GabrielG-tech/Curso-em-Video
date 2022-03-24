print('{:=^40}'.format(' DESAFIO 49 '))
num = int(input('Tabuada de: '))
n = 0
for c in range(0, num*11, num):
    print('{} x {} = {}'.format(num, n, num * n))
    n += 1
