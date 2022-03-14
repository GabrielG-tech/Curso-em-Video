print('='*12 + ' DESAFIO 44 ' + '='*12)
preço = float(input('Preço do produto: '))
print('''Escreva o número correspondente a formas de pagamento:
- Dinheiro ou chegue (10% de desconto) [1]
- À vista no cartão (5% de desconto) [2]
- Em até 2x no cartão [3]
- 3x ou mais no cartão (20% de juros) [4]''')
forma_de_pagamento = int(input('Formar de pagamento: '))
if forma_de_pagamento == 1:
    valor = preço - preço * 10 / 100
elif forma_de_pagamento == 2:
    valor = preço - preço * 5 / 100
elif forma_de_pagamento == 3:
    valor = preço
elif forma_de_pagamento == 4:
    valor = preço + preço * 20 / 100
print('\nO produto custará \033[1;32mR${:.2f}\033[m.'.format(valor))
