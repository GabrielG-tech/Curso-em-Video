print('='*12 + ' DESAFIO 38 ' + '='*12)
n1 = int(input('Escreva o primeiro valor para comparação: '))
n2 = int(input('Escreva o segundo valor para comparação: '))
lista = [n1, n2]
if n1 == n2:
    print('Não existe valor maior, os dois são iguais.')
elif n1 > n2:
    print('O Primeiro valor ({}) é o maior.'.format(max(lista)))
elif n2 > n1:
    print('O Segundo valor ({}) é o maior.'.format(max(lista)))
else:
    print('Não existe valor maior, os dois são iguais.')
