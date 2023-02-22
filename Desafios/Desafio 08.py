# Converter metros em centímetros e milímetros

m = int(input('Digite a quantidade de metros: '))
# print('{} metros tem'.format(m), m * 100, 'centímetros e', m * 1000, 'milímetros')
print('Convertendo {} metros, ele possui:'.format(m), '{} kilômetros'.format(m * 0.001),
      ',{} hectómetros'.format(m * 0.01),
      ',{} decâmetros'.format(m * 0.1), ',{} decímetros'.format(m * 10), ',{} centímetros'.format(m * 100),
      'e {} milímetros.'.format(m * 1000))
