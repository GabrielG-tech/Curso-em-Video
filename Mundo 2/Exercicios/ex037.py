print('='*12 + ' DESAFIO 37 ' + '='*12)
num = int(input('Número um número inteiro para conversão: '))
print('''Escolha uma das bases para conversão
[ 1 ] converter para Binário
[ 2 ] converter para Octal
[ 3 ] converter para Hexadeciamal''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para Binário é igual a {}.'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para Octal é igual a {}.'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para Hexadeciamal é igual a {}.'.format(num, hex(num)[2:]))
else:
    print('\033[31m*Opção inválida, Tente Novamente*\033[m')
