print('{:=^40}'.format(' DESAFIO 54 '))
from datetime import date
maior_idade = 18
pessoas = 4
maiores = 0
for c in range(0, pessoas):
    ano = int(input('Digite seu ano de nascimento: '))
    if date.today().year - ano >= maior_idade:
        maiores = maiores + 1
menores = pessoas - maiores
print('Maiores de idade: {}\nMenores de idade: {}'.format(maiores, menores))
