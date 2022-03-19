print('='*12 + ' DESAFIO 45 ' + '='*12)
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
bot = randint(0,2)
print('-='*20)
print('         Vamos jogar Jokenpô!')
print('-='*20)
print(' [ 0 ] para Pedra\n [ 1 ] para Papel\n [ 2 ] para Tesoura')
jogo = int(input('Faça sua jogada: '))
print('Bot jogou {}'.format(itens[bot]))
print('Jogador jogou {}'.format(itens[jogo]))
#if jogo == 1 and bot == 1 or jogo == 2 and bot == 2 or jogo == 3 and bot == 3:
#    resultado = '\033[1;33mEmpate, Bom jogo!\033[m'
#elif jogo == 1 and bot == 2 or jogo == 2 and bot == 3 or jogo == 3 and bot == 1:
#    resultado = '\033[1;31mVitoria do Bot, Bom jogo!\033[m'
#elif jogo == 2 and bot == 1 or jogo == 3 and bot == 2 or jogo == 1 and bot == 3:
#    resultado = '\033[1;32mVitória do Jogador, Parabéns!!\033[m'
#if bot == 1: botx = 'Pedra'
#elif bot == 2: botx = 'Papel'
#elif bot == 3: botx = 'Tesoura'
#print('Jo', 'ken', 'pô')
#print('-=' * 11)
#print('''Computador jogou {}
#Jogador jogou {}'''.format(botx, jogo))
#print('-=' * 11)
#print(resultado)
