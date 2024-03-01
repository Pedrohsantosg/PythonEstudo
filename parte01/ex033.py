print('Digite os números a seguir: ')
n1 = int(input('Primeiro Número: '))
n2 = int(input('Segundo Número: '))
n3 = int(input('Terceiro Número: '))
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
    
print('O menor Número %d é o menor' %menor)

maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3

print('O maior Número %d é o maior' %maior)
     

