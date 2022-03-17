print('='*12 + ' DESAFIO 43 ' + '='*12)
print('-='*20)
print('Medidor de Massa Corporal Ideal')
print('-='*20)
peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))
IMC = peso/(altura**2)
if IMC < 18.5:
    result = '\033[4;33mabaixo do Peso\033[m.'
elif 18.5 <= IMC <= 25:
    result = 'de \033[32mPeso ideal\033[m.'
elif 25 < IMC <= 30:
    result = 'de \033[33mSobrepeso\033[m.'
elif 30 < IMC <= 40:
    result = 'de \033[4;31mObesidade\033[m.'
else:
    result = '\033[1;31mObesidade mórbida, Cuidado!\033[m'
print('Seu IMC (Índice de Massa Corporal) é de {:.2f} kg/m².'.format(IMC))
print('Você esta na faixa {}'.format(result))
