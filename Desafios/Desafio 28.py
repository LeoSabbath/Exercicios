# Usuário tenta adivinhar um número de 0 a 5 gerado pelo computador

from random import randint
from time import sleep

n = randint(0, 5)

print('Um número foi gerado!')
x = int(input('Escolha um número de 0 à 5: '))
print('\033[33mPROCESSANDO...')
sleep(2)
if x == n:
    print('\033[32mParabéns! Você acertou!')
else:
    print('\033[31mNúmero errado! Eu gerei o número {} e você digitou {}.'.format(n,x))
