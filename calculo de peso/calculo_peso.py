
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = peso / (altura ** 2)
if imc < 18.5:
  print("Pessoa abaixo do peso")
elif imc < 25:
   print("Pessoa acima do peso")
elif imc < 30:
   print("Pessoa acima do peso")
else:
    print("Pessoa Obesa")







#Criei um programa que calcule o peso ideal de uma pessoa. Para isso utilize as fórmulas da tabela:

#Para Homens: (72.7 * altura) – 58
#Para Mulheres: (62.1 * altura) – 44.7 

#Sua aplicação deve identificar se a pessoa é Homem ou Mulher e então fazer o cálculo apropriado.
#  Deve ser impresso se a pessoa é homem ou mulher, juntamente com o peso ideal calculado.


