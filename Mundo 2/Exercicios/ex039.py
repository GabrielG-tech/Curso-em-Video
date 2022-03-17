print('='*12 + ' DESAFIO 39 ' + '='*12)
print('''Digite o corespondente do seu sexo: 
[ 1 ] Masculino
[ 2 ] Feminino''')
sexo = int(input('Resposta: '))
if sexo == 2:
    print('Você não precisa se alistar obrigatório.')
else:
    from datetime import date
    ano = int(input('Ano de nascimento: '))
    idade = date.today().year - ano
    if idade < 18:
        if (18 - idade) != 1:
            s = 's'
            m = 'm'
        else:
            s = ''
            m = ''
        print('Ainda falta{} {} ano{}. Será em {}.'.format(m, 18 - idade, s, 18 + ano))
    elif idade == 18:
        print('É hora de se alistar agora em {}.'.format(date.today().year))
    else:
        if (idade - 18) != 1:
            s = 's'
        else:
            s = ''
        print('Você já deveria ter se alistado faz {} ano{}.'.format(idade - 18, s))
        print('Deveria ter sido em {}.'.format(date.today().year - (idade - 18)))
