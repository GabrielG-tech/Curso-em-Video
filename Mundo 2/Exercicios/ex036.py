print('='*12 + ' DESAFIO 36 ' + '='*12)
casa = int(input('Valor da casa: R$'))
salario = int(input('Salario do comprador: R$'))
anos = int(input('Por quantos anos deseja parcelar: '))
prest = casa / (anos * 12)
if prest <= salario * 0.3:
    print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
    print('a prestação será de R${:.2f}.'.format(prest))
    print('Empréstimo foi \033[1;32mconcedido\033[m! por mês.')
else:
    print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
    print('a prestação será de R${:.2f}.'.format(prest))
    print('Empréstimo foi \033[1;31mnegado\033[m!')
