# Escolhe aleatoriamente 1 dos 4 nomes digitados.
import random

a = str(input('Digite o nome do primeiro aluno: '))
b = str(input('Digite o nome do segundo aluno: '))
c = str(input('Digite o nome do terceiro aluno: '))
d = str(input('Digite o nome do quarto aluno: '))
lista = [a, b, c, d]
escolhido = random.choice(lista)

print('O escolhido a apagar o quadro foi {}'.format(escolhido))
