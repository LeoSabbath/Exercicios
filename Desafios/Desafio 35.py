# Dado o comprimento de 3 retas, informa se é possível formar um triângulo

primeiro = float(input('Digite o primeiro comprimento de reta: '))
segundo = float(input('Digite o segundo comprimento de reta: '))
terceiro = float(input('Digite o terceiro comprimento de reta: '))

somaab = primeiro + segundo
somaac = primeiro + terceiro
somabc = segundo + terceiro

if (somaab > terceiro) and (somaac > segundo):
    print('\033[32mCom esses três comprimentos é possível fazer um triângulo')
else:
    print('\033[31mCom esses três comprimentos não é posível fazer um triângulo')

