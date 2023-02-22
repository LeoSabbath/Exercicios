# Verifica a velocidade do carro e se for acima de 80km/h aplica munta de R$7,00 por km

velo = int(input('Qual a velocidade do carro?: '))
if velo > 80:
    print('\033[31mVocê foi multado!\033[m')
    acima = velo - 80
    multa = acima * 7
    print('O valor da multa é de \033[31mR${:.2f}'.format(multa))
else:
    print('\033[32mVelocidade permitida!')




