#Reajuste Salarial

#Faça um algoritmo que leia o salário de um funcionário e mostre o seu novo salário, com aumento de 15%

salário_atual = float(input('Qual é o teu salário atual? kz '))
salário_novo = salário_atual + (salário_atual * 15 / 100)
print('O seu salário com o aumento de 15% será {}'.format(salário_novo))