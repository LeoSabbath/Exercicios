# Calcula novo salário aumentado (10% para salários R$1.250,00 + e 15% para R$1.250,00 -)

salario = float(input('Digite o seu salário: R$'))
if salario > 1250:
    novo_salario = salario + salario * 10 / 100
else:
    novo_salario = salario + salario * 15 / 100

print('O seu novo salário será R${:.2f}'.format(novo_salario))
