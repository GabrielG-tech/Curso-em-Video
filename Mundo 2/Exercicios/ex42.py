print('='*12 + ' DESAFIO 42 ' + '='*12)
print('-='*20)
print('Analisandor de Triângulos')
print('-='*20)
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
lista = [s1, s2, s3]
if max(lista) <= (sum(lista) - max(lista)):
    if s1 == s2 == s3:
        print('Este triângulo é \033[1mEquilátero\033[m.')
    if s1 == s2 != s3 or s2 == s3 != s1 or s3 == s1 != s2:
        print('Este triângulo é \033[1mIsósceles\033[m.')
    if s1 != s2 != s3:
        print('Este triângulo é \033[1mEscaleno\033[m.')
else:
    print('\033[31mEstes segmentos não formam um triângulo.\033[m')
