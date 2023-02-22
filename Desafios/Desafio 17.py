# Calcula o comprimento da hipotenusa

import math

o = float(input('Digite o cateto oposto: '))
a = float(input('Digite o cateto adjacente: '))
h = math.hypot(o, a)

print('O comprimento da hipotenusa é {:.2f}'.format(h))
