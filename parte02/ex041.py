from datetime import date
ano = int(input('Ano de Nascimento: '))
atual = date.today().year
calculo = atual - ano

print(f'O atleta tem {calculo}')
if calculo < 9:
    print('CLassificação: Mirim')
elif calculo <=14:
    print('CLassificação: Infantil')
elif calculo <= 19:
    print('CLassificação: Júnior')
elif calculo <= 25:
    print('CLassificação: Sênior')
else:
    print('CLassificação: Master')
