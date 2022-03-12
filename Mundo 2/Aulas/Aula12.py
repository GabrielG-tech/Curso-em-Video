# Para condições aninhadas use 'elif'
n = int(input('Quantos anos você tem? '))
if n <= 17:
    print('Você é bem novo ainda.')
elif n == 18:
    print('Você já é um adulto, parabéns!')
elif 18 < n < 40:
    print('Parace que você é um adulto, tenha um bom dia!')
else:
    print('Ih parace que você já está velinho, tenha um bom dia!')
