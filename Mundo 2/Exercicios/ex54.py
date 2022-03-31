print('='*14 + ' DESAFIO 54 ' + '='*14)
from datetime import date
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Digite seu ano de nascimento: '))
    idade = date.today().year - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade\nE também tivemos {} pessoas menores de idade.'.format(totmaior, totmenor))
