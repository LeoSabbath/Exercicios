# Le um nome de uma cidade e diz se ela começa ou não com a palavra "Santo"

cidade = input('Digite o nome da sua cidade: ')
titlo = cidade.title()
dividido = titlo.split()

print('Santo' in dividido[0])
