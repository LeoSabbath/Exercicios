print('\033[4;31;42mOlá mundo!\033[m')


a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a, b))

nome = 'Leonardo'
print('Olá! Muito prazer em te conhecer {}{}{}'.format('\033[4;31m', nome, '\033[m'))

nome = 'Leonardo'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;97m'}
print('Olá! Muito prazer em te conhecer {}{}{}!!'.format(cores['pretoebranco'], nome, cores['limpa']))




