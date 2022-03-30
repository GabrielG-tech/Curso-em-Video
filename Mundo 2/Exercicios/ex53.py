print('{:=^40}'.format(' DESAFIO 53 '))
n = str(input('Digite uma frase para análise: '))
n = n.lower().strip().split()
n = ''.join(n)
if len(n) % 2 == 0:
    print(n.split(n))
#    resultado = 'Esta frase é um palindromo.'
else:
    print('Fail')
#    resultado = 'Esta frase não é um palindromo.'
