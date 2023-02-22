# Calcula a área de uma parede e quantos litros são necessários para pintá-la

l = float(input('Qual a largura da parede: '))
a = float(input('Qual a altura da parede: '))

area = l * a
t = area / 2

print('A parede possui {} metros quadrados e são necessários {} litros de tinta'.format(area, t))
