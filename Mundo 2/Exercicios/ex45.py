print('='*12 + ' DESAFIO 45 ' + '='*12)
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
bot = randint(0,2)
print('-='*12)
print('  Vamos jogar Jokenpô!')
print('-='*12)
print('[ 0 ] para Pedra\n[ 1 ] para Papel\n[ 2 ] para Tesoura')
jogador = int(input('Faça sua jogada: '))
print('Jo')
sleep(0.8)
print('ken')
sleep(0.8)
print('po!!!')
sleep(0.8)
print('-='*12)
print('Jogador jogou {}'.format(itens[jogador]))
print('Computador jogou {}'.format(itens[bot]))
print('-='*12)
if bot == 0:
    if jogador == 0:
        print('\033[1;33mEmpate, Bom jogo!\033[m')
    elif jogador == 1:
        print('\033[1;32mVitória do Jogador, Parabéns!!\033[m')
    elif jogador == 2:
        print('\033[1;31mVitoria do Bot, Bom jogo!\033[m')
    else:
        print('\033[1;31mJogada inválida, tente novamente.\033[m')
elif bot == 1:
    if jogador == 0:
        print('\033[1;31mVitoria do Bot, Bom jogo!\033[m')
    elif jogador == 1:
        print('\033[1;33mEmpate, Bom jogo!\033[m')
    elif jogador == 2:
        print('\033[1;32mVitória do Jogador, Parabéns!!\033[m')
    else:
        print('\033[1;31mJogada inválida, tente novamente.\033[m')
elif bot == 2:
    if jogador == 0:
        print('\033[1;32mVitória do Jogador, Parabéns!!\033[m')
    elif jogador == 1:
        print('\033[1;31mVitoria do Bot, Bom jogo!\033[m')
    elif jogador == 2:
        print('\033[1;33mEmpate, Bom jogo!\033[m')
    else:
        print('\033[1;31mJogada inválida, tente novamente.\033[m')
