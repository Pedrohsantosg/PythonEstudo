v = float(input('Quantos é a distancia da sua viagem? '))
'''if v < 200 :
    c = v*0.50
    print('O valor da sua passagem será de R${:.2f}'.format(c))
else:
    c = v*0.45
    print('O valor da sua passagem será de R${:.2f}'.format(c))
'''
preco = v*0.50 if v <= 200 else v*0.45
print('O valor da sua passagem será de {:.2f}'.format(preco))
