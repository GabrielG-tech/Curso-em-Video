print('='*12 + ' DESAFIO 41 ' + '='*12)
from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    classe = 'Mirim'
elif 9 < idade <= 14:
    classe = 'Infantil'
elif 14 < idade <= 19:
    classe = 'Junior'
elif 19 < idade <= 20:
    classe = 'Sênior'
else:
    classe = 'Master'
print('Sua classificação é {}.'.format(classe))

