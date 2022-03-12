num = int(input('Número para conversão: '))
sist = int(input('Digite [1] para Binário, [2] para Octal e [3] para Hexadecimal: '))
if sist == 1:
    n = bin(num)
    print(n)
    x = 'Binário'
elif sist == 2:
    n = oct(num)
    print(n)
    x = 'Octal'
elif sist == 3:
    n = hex(num)
    print(n)
    x = 'Hexadecimal'
print('O número {} é igual a {} em {}'.format(num, n, x))
