import math
angulo = float(input('Qual o valor do seu ângulo: '))
seno = math.sin(math.radians(angulo))
coss = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo,coss))
print('O angulo de {} tem o SENO de {:.2f}'.format(angulo,seno))
print('O tangulo de {} tem a TANGENTE de {:.2f}'.format(angulo,tang))
