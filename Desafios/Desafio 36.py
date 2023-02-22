# Calcula o valor da prestação de compra de uma casa

print('\033[34;45mCompre a sua casa!\033[m')
casa = float(input('Digite o valor da casa R$: '))
salario = float(input('Digite o valor do seu salário R$:'))
meses = int(input('Em quantos meses gostaria de pagar a casa?: '))
print()

prestacao = casa / meses

if prestacao < salario * 30 / 100:
    print('\033[32mCompra permitida. PARABÉNS!')
    print('O valor da sua prestação é de R${:.2f}'.format(prestacao))
else:
    print('\033[31mCompra Negada!')
    print('Infelizmente o valor da prestação ultrapassa 30% do seu salário.')
