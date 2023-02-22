# Calcula o novo preço de um produto com 5% de desconto

p = float(input('Digite o preço do produto: R$'))
d = p - (p * 5/100)
print('O novo preço com 5% de desconto é R${:.2f}'.format(d))
