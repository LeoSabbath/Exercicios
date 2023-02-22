# O programa diz qual o maior numero inteiro entre os 2 digitados

primeiro = int(input('Digite o primeiro número: '))
segundo = int(input('Digite o segundo número: '))

if primeiro > segundo:
    print('O {} é o maior número!'.format(primeiro))
elif segundo > primeiro:
    print('O {} é o maior número!'.format(segundo))
else:
    print('Não existe número maior! Os dois números são iguais.')