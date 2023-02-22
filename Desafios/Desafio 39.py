# Mostra se ainda precisa se alistar, se está na hora ou se passou.

from datetime import datetime
now = datetime.now()
ano = now.year

nascimento = int(input('Digite o seu ano de nascimento: '))
if ano - nascimento < 18:
    precisa = 18 - (ano - nascimento)
    print('\033[32mVocê ainda precisa se alistar! Faltam {} anos.'.format(precisa))
elif ano - nascimento == 18:
    print('\033[33mEstá no ano de você fazer o seu alistamento!')
else:
    passou = 18 - (ano - nascimento)
    print('\033[31mJá passou o seu ano de alistamento! Se passaram {} anos.'.format(abs(passou)))


