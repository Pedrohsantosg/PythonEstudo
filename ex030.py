from time import sleep
n = int(input('Me diga um número qualquer: '))
print('Verificando se é par ou ímpar..')
sleep(2)
if n%2 == 0:
    print('Par!')
elif n%2 == 1:
    print('Ímpar!')
