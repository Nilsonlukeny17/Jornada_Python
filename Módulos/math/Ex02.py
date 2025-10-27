# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

ângulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ângulo))
cosseno = math.cos(math.radians(ângulo))
tangente = math.tan(math.radians(ângulo))

print('O ângulo de {} tem o seno de {:.2f}'.format(ângulo, seno))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(ângulo, cosseno))
print('O ângulo de {} tem a tangente de {:.2f}'.format(ângulo, tangente))

# Posso também chamar directamente as funções que pretendo usar
from math import sin, cos, tan, radians

ângulo = float(input('Digite o ângulo que você deseja: '))
seno1 = sin(radians(ângulo))
cosseno2 = cos(radians(ângulo))
tangente3 = tan(radians(ângulo))

print('O ângulo {} tem o seno de {:.2f}'.format(ângulo, seno1))
print('O ângulo {} tem o cosseno de {:.2f}'.format(ângulo, cosseno2))
print('O ângulo {} tem a tangente de {:.2f}'.format(ângulo, tangente3))