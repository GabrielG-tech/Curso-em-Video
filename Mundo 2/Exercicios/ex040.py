print('='*12 + ' DESAFIO 40 ' + '='*12)
n1 = int(input('Digite sua 1º nota: '))
n2 = int(input('Digite sua 2º nota: '))
media = (n1 + n2)/2
if media < 5.0:
    print('\033[1;31m ---== REPROVADO ==--- \033[m')
elif 5.0 <= media <= 6.9:
    print('\033[1;33m ---== RECUPERAÇÃO ==--- \033[m')
else:
    print('\033[1;32m ---== APROVADO ==--- \033[m')

