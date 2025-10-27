#Calculando descontos

#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com desconto de 5%

"""Encontrar percentagem : 100kz ---- 100%
                             Xkz ----  5%
X - representa o valor a ser encontrando, no caso, o valor real de quanto é 5%
Depois é so fazer sistema cruzado e encontrar o x. Quando encontrar, basta subtrair com o valor real do produto (desconto), ou aumentar com o valor
real do produto (aumento)
Ex.: 100 - 5
     100 + 5
"""
preço = float(input('Qual é o preço do produto? kz'))
novo = preço - (preço * 5 / 100)
print('O produto custava {:.2f}, com o desconto  de 5% vai custar {:.2f}kz'.format(preço, novo))