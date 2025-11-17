''' Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo'''

# Matematicamente, três retas formam sempre um triângulo quando 'cada um desses segmentos tem que ser menor que a soma dos comprimentos dos outros dois'

r1 = float(input('Digite o primeiro segmento de reta: '))
r2 = float(input('Digite o segundo segmento de reta: '))
r3 = float(input('Digite o terceiro segmento de reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2: # Condição matemática para saber!
    print('As retas que inseriste PODEM formar um triângulo')
else:
    print('As retas que inseriste NÃO PODEM formar um triângulo')
