# Le um frase e diz quantas letra "A" possui, qual a posição que a letra "A" aparece da primeira
# vez e qual a última vez que ela aparece.

frase = str(input('Digite uma frase: ')).upper().strip()

print('A frase possui {} letras "A"'.format(frase.count('A')))
print('A primeira vez que a letra "A" aparece na frase é na posição {}'.format(frase.find('A')+1))
print('A última vez que a letra "A" aparece na frase é na posição {}'.format(frase.rfind('A')+1))


