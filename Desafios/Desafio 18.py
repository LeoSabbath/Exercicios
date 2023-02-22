# Lê um ângulo e calcula o seu seno, cosseno e tangente

import math

a = float(input('Digite o ângulo: '))

b = math.radians(a)
s = math.sin(b)
cos = math.cos(b)
t = math.tan(b)

print('O ângulo do seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(s, cos, t))

