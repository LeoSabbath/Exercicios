# Seleciona uma sequencia de ordem dos nomes digitados

import random

a = str(input('Digite o nome do primeiro aluno: '))
b = str(input('Digite o nome do segundo aluno: '))
c = str(input('Digite o nome do terceiro aluno: '))
d = str(input('Digite o nome do quarto aluno: '))

lista = [a, b, c, d]

random.shuffle(lista)

print('A ordem de apresentação será {}'.format(lista))