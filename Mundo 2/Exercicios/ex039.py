print('='*12 + ' DESAFIO 39 ' + '='*12)
from datetime import date
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
if idade < 18:
    print('Ainda não é hora de se alistar, Ainda faltam {} anos.'.format(18 - idade))
elif idade == 18:
    print('É hora de se alistar.')
else:
    print('Já passou da hora de se alistar faz {} anos.'.format(idade - 18))

