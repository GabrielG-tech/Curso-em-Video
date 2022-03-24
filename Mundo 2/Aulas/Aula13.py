from time import sleep
#n = int(input('Escreva um número: '))
#for c in range(n, 0, -1):
#    print(c)
#    sleep(0.4)
#print('\033[1;31mFim\033[m')

#i = int(input('Início: '))
#f = int(input('Fim: '))
#p = int(input('Passo: '))
#for c in range(i, f+1, p):
#    print(c)
#    sleep(0.8)
#print('Fim')

s = 0
for c in range(0, 4):
    sleep(0.8)
    n = int(input('Digite um valor: '))
#   s = s + n
    s += n
print('O somatório de todos os números é {}.'.format(s))
