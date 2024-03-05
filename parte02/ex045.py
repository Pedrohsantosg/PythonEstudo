import time, random
itens = ('Pedra', 'Papel', 'Tesoura' )
computador = random.randint(0,2)
print(''' Suas opções
      [0] PEDRA
      [1] PAPEL
      [2] TESOURA
      ''')
opcao = int(input('Qual a sua opção: '))
print('...')
print('JO')
time.sleep(1.5)
print('KEN')
time.sleep(1)
print('PO')
print('-='*11)
print('Computador escolheu {}'.format(itens[computador]))
print('Jogador escolheu {}'.format(itens[opcao]))
print('-='*11)
if computador == 0:
    if opcao == 0:
        print('EMPATE')
    elif opcao == 1:
        print('JOGADOR VENCE')
    elif opcao == 2:
        print('COMPUTADOR VENCE')
elif computador == 1:
    if opcao == 0:
        print('COMPUTADOR VENCE')
    elif opcao == 1:
        print('EMPATE')
    elif opcao == 2:
        print('JOGADOR VENCE')
elif computador == 2:
    if opcao == 0:
        print('JOGADOR VENCE')
    elif opcao == 1:
        print('COMPUTADOR VENCE')
    elif opcao == 2:
        print('EMPATE')
else:
    print('Opção inválida! Encerrando programa')
        
