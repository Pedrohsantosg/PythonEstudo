casa = float(input('Valor da casa: R$ '))
salario = float(input('Salario do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))

prestacao = casa/(anos * 12)
min = salario * 30/100

print('Para pagar uma casa de R$%.2f em %d anos' %(casa, anos), end='')
print(' A prestação será de R$%.2f' %prestacao)
if prestacao <= min:
    print('Empréstmo pode ser   concedido')
else:
    print('Empréstimo não pode ser concedido')
