print('='*12 + ' DESAFIO 38 ' + '='*12)
pv = int(input('Escreva o primeiro valor para comparação: '))
sv = int(input('Escreva o segundo valor para comparação: '))
lista = [pv, sv]
if pv == sv:
    print('Não existe valor maior, os dois são iguais.')
else:
    print('O {} é o maior número'.format(max(lista)))
    print('O {} é o menor número'.format(min(lista)))
