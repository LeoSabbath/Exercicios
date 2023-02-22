#Calcula valor do aluguel de um carro com base nos km/dias alugados

x = int(input('Por quantos dias o carro foi alugado?: '))
y = float(input('Quantos kilômetros foram rodados pelo carro?: '))

dias = x * 60
km = y * 0.15
total = dias + km

print('O valor a ser pago é de R${:.2f}'.format(total))


