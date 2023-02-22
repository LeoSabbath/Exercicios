# Informe os km da viagem para saber o valor (R$0,50 até 200km e R$0,45 para 200km+)

print('\033[31;40mFrota Sabbath\033[m')
d = int(input('Qual a distância da viagem?: '))

if d < 201:
    valor = d * 0.5
    print('O valor da viagem é de R${:.2f}'.format(valor))
else:
    valor = d * 0.45
    print('O valor da viagem é de R${:.2f}'.format(valor))
