print('{:=^40}'.format('LOJA'))
valor = float(input('Preço das compras: R$'))
print('''Formas de Pagamento
[1] á vista dinehiro/cheque
[2] á vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
      ''')
opcao = int(input('Qual a opção: '))
match opcao:
    case 1:
        total = valor - (valor * 10 / 100)
        print('Sua compra de R${:.2f} custará R${:.2f} com desconto de 10%'.format(valor, total))
    case 2:
        total = valor - (valor * 5 / 100)
        print('Sua compra de R${:.2f} custará R${:.2f} com desconto de 5%'.format(valor, total))
    case 3:
        total = valor
        print('Sua compra de R${:.2f} custará R${:.2f} sem desconto'.format(valor, total))
    case 4:
        total = valor + (valor * 20 / 100)
        print('Sua compra de R${:.2f} custará R${:.2f} com juros de 20%'.format(valor, total))
    case _:
        print('Opção Inválida!')
    