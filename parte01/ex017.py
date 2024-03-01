import math
co = float(input('Qual o valor do Cateto Oposto: '))
ca = float(input('Qual  o valor do Cateto Adjacente: '))
hi = math.hypot(co,ca)
hip = (co**2 + ca **2) **(1/2)
print ('A hipotenusa vai medir {:.2f}'.format(hi))
