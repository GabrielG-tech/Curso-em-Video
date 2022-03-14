print('='*12 + ' DESAFIO 42 ' + '='*12)
print('-='*20)
print('Analisandor de Triângulos')
print('-='*20)
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
lista = [s1, s2, s3]
if max(lista) <= (sum(lista) - max(lista)):
    print('Estes segmentos podem formar um triângulo.')
else:
    print('\033[31mEstes segmentos não formam um triângulo.\033[m')
