print('='*12 + ' DESAFIO 43 ' + '='*12)
print('-='*20)
print('Medidor de Massa Corporal Ideal')
print('-='*20)
peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))
IMC = peso/(altura**2)
if IMC < 18.5:
    result = 'Abaixo do Peso'
elif 18.5 <= IMC <= 25:
    result = 'Peso ideal'
elif 25 < IMC <= 30:
    result = 'Sobrepeso'
elif 30 < IMC <= 40:
    result = 'Obesidade'
else:
    result = 'Obesidade mórbida'
print('Seu caso é de: {} [{:.2f}kg/m²].'.format(result, IMC))

