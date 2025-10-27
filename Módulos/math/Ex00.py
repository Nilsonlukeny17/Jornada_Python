
"""Crie um programa que leia um número real e qualquer pelo teclado e mostre na tela a sua porçao inteira
Ex.: Digite um número: 6.127
O número 6.127 tem a parte inteira 6.
"""
import math
# from math import trunc

# Opção 1.
num = float(input('Digite um número: '))
parte_inteira = math.trunc(num)
print('A parte inteira do valor digitado é {}'.format(parte_inteira))

# Opção 2 - (Funciona quando chamamos directamente a 'função' com *from math import trunc*)
'''num = float(input('Digite um número: '))
print('A parte inteira do número digitado é {}'.format(trunc(num)))'''