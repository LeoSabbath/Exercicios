# Converte o novo salário de um funcionário com o aumento de 15%

s = float(input('Digite o seu salário atual: R$'))
n = s + (s * 15/100)
print('O seu novo salário com o aumento de 15% é de R${:.2f}'.format(n))
