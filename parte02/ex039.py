from datetime import date
atual = date.today().year
nasc = int(input('Em que ano você nasceu? '))
idade = atual - nasc
print('Quem nasceu em %d tem %d anos em %d ' % (nasc, idade, atual))
if idade  == 18 :
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Você já deveria ter se alistado há {} anos!'.format(saldo))
    ano = atual + saldo
    print('Seu alisatamento será em {}' .format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos!'.format(idade - 18))
    ano = atual - saldo
    print('Seu alisatamento será em {}'.format(ano))

