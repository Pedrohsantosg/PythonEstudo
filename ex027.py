n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Prazer em te conhecer!')
print('O seu primeiro nome é {} e o último é {}'.format(nome[0], nome[len(nome)-1]))
