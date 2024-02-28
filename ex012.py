preco = float(input('Qual o valor do produto? R$'))
desconto = int(input('Quanto de desconto você quer aplicar do produto: '))
valor = preco - (preco *(desconto/100))
print('O produtop que custava R${:.2f}, na promoção escolhida de {}% vai custar R${:.2f}'.format(preco,desconto,valor))
