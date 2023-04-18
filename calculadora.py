#Tabela de impostos IRRF da Receita Federal em 2023:

#até 1.903,98 => Isento.
#de 1.903,99 a 2.826,65 => 7,5% - 142,80.
#de 2.826,66 a 3.751,05 => 15% - 354,80.
#de 3.751,06 a 4.664,68 => 22,5% - 636,13.
#acima de 4.664,68 - 27,5% => 869,36.


salario = float(input('digite seu salario: '))

if salario <= 1903.99:
   print ('voce esta isento do imposto de renda!')

elif salario >= 1903.99 and salario <= 2826.65:
  salario_atual = salario -(0.075 * salario) + 142
  print ('seu salario apos desconto sera de: ', salario_atual)
  
elif salario >= 2826.66 and salario <= 3751.05:
  salario_atual = salario - (0.15 * salario) + 354.80
  print ('seu salario apos desconto sera de: ', salario_atual)
  
elif salario >= 3751.06 and salario <= 4664.68:
  salario_atual = salario - (0.225 * salario) + 636.13
  print ('seu salario apos desconto sera de: ', salario_atual)
  
elif salario >= 4664.69:
  salario_atual = salario - (0.275 * salario) + 869.36  
print ('seu salario apos desconto sera de: ', salario_atual)
