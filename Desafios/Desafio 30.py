# Informe um número inteiro e o programa informa se é par ou ímpar

n = int(input('\033[7;97;40mDigite um número: \033[m'))

if n % 2 == 0:
    print('Esse número é par!')
else:
    print('Esse número é ímpar!')