print('{:=^40}'.format(' DESAFIO 46 '))
from time import sleep
import emoji
for c in range(10, 0, -1):
    print(c)
    sleep(0.45)
fogos = emoji.emojize("\033[1;31m:fireworks: \033[m") * 11
print(fogos)
print('\033[1;31m{}Fogos de artifício {}\033[m'.format(emoji.emojize(":fireworks: ") * 2, emoji.emojize(":fireworks: ") * 2))
print(fogos)
