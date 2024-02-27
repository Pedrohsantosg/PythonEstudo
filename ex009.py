nFixo = int(input('Digite um número para ver sua tabuada --> '))
nVariael = 0 
print('-'*12)
while (nVariael <= 10):
    print('{:2} x {:2} = {:2}'.format(nFixo, nVariael, (nFixo*nVariael)))
    nVariael += 1
print('-'*12)

