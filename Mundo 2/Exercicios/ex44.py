print('{:=^40}'.format(' DESAFIO 44 '))
preço = float(input('Preço do produto: R$'))
print('''Escreva o número correspondente a formas de pagamento:
[ 1 ] Dinheiro ou chegue
[ 2 ] À vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Opção: '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantidade de parcelas: '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} com \033[1mjuros\033[m.'.format(totparc, parcela))
else:total = preço
print('\033[1;31mOpção inválidade de pagamento. Tente Novamente!\033[m')
print('Sua compra de {}, custará no total \033[1mR${:.2f}\033[m.'.format(preço, total))
