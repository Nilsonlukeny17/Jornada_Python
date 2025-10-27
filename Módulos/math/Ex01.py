'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo rectângulo,
calcule e mostre o comprimento da hipotenusa'''

import math

c_oposto = float(input('Digite o valor do cateto oposto: '))
c_adjacente = float(input('Digite o valor do cateto adjacente: '))
hi = math.hypot(c_oposto, c_adjacente)

print('O comprimento da hipotenusa é {:.2f} '.format(hi))