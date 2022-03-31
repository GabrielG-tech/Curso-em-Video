print('='*14 + ' DESAFIO 56 ' + '='*14)
pessoa = 0
somaidade = 0
idademax = 0
velho = ''
menina = 0
for p in range(1, 5):
    pessoa += 1
    print('-' * 5 + ' {}ª Pessoa '.format(pessoa) + '-' * 5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    if sexo == 'M' or 'm' and p == 1:
        idademax = idade
    if sexo == 'M' or 'm' and idade > idademax:
        idademax = idade
        velho = nome
    if sexo == 'F' or 'f':
        if idade < 20:
            menina += 1
    somaidade += idade
media = somaidade/pessoa
print('A média de idade do grupo é de {} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(idademax, velho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(menina))
