# Digite o ano de nascimento para descobrir a categoria do atleta

from datetime import datetime
now = datetime.now()
ano = now.year

nascimento = int(input('Digite o ano de nascimento: '))

if ano - nascimento < 10:
    print('Você está na categoria MIRIM!')
elif ano - nascimento < 15:
    print('Você está na categoria INFANTIL!')
elif ano - nascimento < 20:
    print('Você está na categoria JUNIOR!')
elif ano - nascimento == 20:
    print('Você está na categoria SÊNIOR!')
else:
    print('Você está na categoria MASTER!')


