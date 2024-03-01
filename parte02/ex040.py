nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Segundo Nota: '))
media = (nota1 + nota2)/2
print('Tirando {:.1f} e {:.1f}, a media do aluno é {:.1f}'.format(nota1, nota2, media))
if media < 5:
    print('Reprovado')
elif media > 5 and media < 6.9 :
    print('Recuperação')
else :
    print('Aprovado')
