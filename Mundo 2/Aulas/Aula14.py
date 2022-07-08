# Aula 14 – Estrutura de repetição while
sim_nao = 'S'
par = impar = 0
while sim_nao == 'S':
    n = int(input('Digite um valor: '))
    sim_nao = str(input('Quer continuar? [S/N] ')).upper()
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números impares.'.format(par, impar))
