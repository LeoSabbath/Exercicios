# Pede o nome completo e mostra o nome com todas as letras maúsculas, minúsculas, quantas
# letras no total (sem contas  espaço e quantas letras tem o primeiro nome

nome = input('Digite o seu nome completo: ').strip()
print(nome.upper())
print(nome.lower())
total = nome.split()
teste = total[0] + total[1]
print(len(teste))
dividido = nome.split()
print(len(dividido[0]))



