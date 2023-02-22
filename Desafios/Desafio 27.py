# Le o nome completo e mostra o primeiro e último nome digitado separadamente

nome = str(input('Digite o seu nome completo: ')).strip()
separado = nome.split()

print('Primeiro nome: {}'.format(separado[0]))
print('Último nome: {}'.format(separado[len(separado)-1]))
