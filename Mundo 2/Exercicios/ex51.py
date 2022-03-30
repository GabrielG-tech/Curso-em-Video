print('{:=^40}'.format(' DESAFIO 51 '))
n = int(input('Digite um número para a progressão: '))
r = int(input('Digite a razão da P.A.: '))
print(n)
for c in range(0, 9):
    n += r
    print(n)
