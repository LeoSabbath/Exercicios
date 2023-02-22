#Lê 3 números e diz qual o maior e o menor

um = int(input('Digite o primeiro número: '))
dois = int(input('Digite o segundo número: '))
tres = int(input('Digite o terceiro número: '))

if (um > dois) and (um > tres):
    maior = 'primeiro'
if (dois > um) and (dois > tres):
    maior = 'segundo'
if (tres > um) and (tres > dois):
    maior = 'terceiro'
print('O {} número é o maior'.format(maior))

if (um < dois) and (um < tres):
    menor = 'primeiro'
if (dois < um) and (dois < tres):
    menor = 'segundo'
if (tres < um) and (tres < dois):
    menor = 'terceiro'
print('O {} número é o menor'.format(menor))

