# Digite o peso e a altura para saber a classificação do IMC

peso = float(input('Digite o seu peso: '))
alt = float(input('Digite a sua altura: '))

imc = peso / (alt * alt)

print('O seu IMC é {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc > 18.4 and imc < 25:
    print('Você está no peso ideal!')
elif imc > 24 and imc < 30:
    print('Você está com sobrepeso!')
elif imc > 29 and imc < 41:
    print('Você está com obesidade!')
else:
    print('Você está com obesidade mórbida!')
