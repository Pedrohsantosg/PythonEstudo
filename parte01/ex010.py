reais = float(input('Quanto de dinheiro você tem na carteira? R$'))
dolar = reais / 4.93
print('Com R${:.2f} você pode comprar US${:.2f}'.format(reais, dolar))
