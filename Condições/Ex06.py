'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a 1.250.00 USD, calcule o aumento de 10%.
Para inferiores ou iguais, o aumento é de 15%. '''

salário = float(input('Qual é o seu salário? '))

if salário > 1250:
    aumento = salário + (salário * 10 / 100)
    percentagem = '10%'
else:
    aumento = salário + (salário * 15 / 100)
    percentagem = '15%'
print('O seu salário com o aumento de {} passará a ser de {}'.format(percentagem, aumento))