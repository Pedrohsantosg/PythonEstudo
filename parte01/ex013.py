salFuncionario = float(input('Qual é o salário do funcionário? R$'))
aumento = int(input('Quanto de aumento você quer determinar no salário: '))
contaSalarial = salFuncionario + (salFuncionario*(aumento/100))
print('O salário que era R${:.2f} com um aumento de {}%, agora está ganhando R${:.2f}.'.format(salFuncionario, aumento, contaSalarial))
      