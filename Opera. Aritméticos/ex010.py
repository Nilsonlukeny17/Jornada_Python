# Aluguel de Carros

"""Escreva um programa que pergunta a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa 12 mil por dia e 100 kzs por Km rodado. 
"""

km = float(input('Quantos km o carro percorreu? '))
dias = int(input('Quantos dias o carro esteve alugado? '))
preço_a_pagar = (km * 100) + (dias * 12000)
print('O carro percorreu {} km'.format(km))
print('O carro esteve alugado durante {} dias'.format(dias))
print('Por isso, o preço a pagar é {}'.format(preço_a_pagar))