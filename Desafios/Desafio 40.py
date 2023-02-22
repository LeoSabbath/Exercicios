# Calcula media entre 2 notas e mostra se esta reprovado, em recuperação ou aprovado

n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))

if (n1 + n2) / 2 < 5:
    print('\033[31mVocê está REPROVADO!')
elif (n1 + n2) / 2 > 5 and (n1 + n2) / 2 < 6.9:
    print('\033[33mVocê está de RECUPERAÇÃO!')
else:
    print('\033[32mParabéns! Você está APROVADO!')
