print('{:=^40}'.format(' DESAFIO 52 '))
n = int(input('Número para análise: '))
x = 0
for c in range(0, 10):
    x = x + 1
    if n % x != 0:
        print('Este número é primo.')
if n % x == 0:
    resposta = 'Este número não é primo.'
print(resposta)
