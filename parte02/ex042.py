s1 = int(input('Primerio Segmento: '))
s2 = int(input('Segundo Segmento: '))
s3 = int(input('Terceiro Segmento: '))

if  s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('As retas podem formar um triângulo', end=' ')
    if s1 == s2 == s3:
        print('Equilátero')
    elif s1 == s2 or s1 == s3 or s2 == s3:
        print('Isósceles')
    else:
        print('Escaleno')
else:
    print('As retas não podem formar um triângulo')
 
