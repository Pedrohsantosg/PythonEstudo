from time import sleep
v = float(input('Qual a velociade atual do carro?'))
print('Verificando se a velocidade atual do carro é válida ou não ....')
sleep(2)
if v <= 80:
    print('Você está dentro da velocidade permitida')
    print('Dirija com segurança')
else:
    multa = (v-80)*7
    print('Você não está dentro da velocidade permitida')
    print('A multa será de R${}, conforme a alta velocidade'.format(multa))
