print('{:=^40}'.format(' DESAFIO 57 '))
sexo = ''
sexo = str(input('Digite seus sexo [M/F]: ')).upper()
while sexo != 'M' or sexo != 'F':
    sexo = str(input('Esta resposta é inválida\nPorfavor digite seus sexo [M/F]: ')).upper()
print(sexo)
