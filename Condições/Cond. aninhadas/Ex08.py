""" Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
"""

peso = float(input('Qual é o teu peso? '))
altura = float(input('Qual é a tua altura? '))
imc = peso / (altura ** 2)

if imc <= 18.5:
    print('Com uma altura de {} e peso de {}, você está ABAIXO DO PESO!'.format(altura, peso))
elif imc <= 25:
    print('Com uma altura de {} e peso de {}, você está com PESO IDEAL!'.format(altura, peso))
elif imc <= 30:
    print('Com uma altura de {} e peso de {} você está com SOBREPESO!'.format(altura, peso))
elif imc <= 40:
    print("Com uma altura de {} e peso de {} você está com OBESIDADE!".format(altura, peso))
else:
    print("Com uma altura de {} e peso de {} você está com OBESIDADE MÓRBIDA!".format(altura, peso))