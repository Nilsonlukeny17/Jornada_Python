'''Escreva um programa que faça o computador pensar num número inteiro entre 0 e 5, e peça para o usuário tentar descobrir qual foi o número
escolhido pelo computador. O programa deverá escrever na tela se o usuário perdeu ou venceu'''

from random import randint
from time import sleep

print('=' * 53)
print('Vou pensar num número entre 0 e 5. Tente adivinhar!')
print('=' * 53)

sorte = randint(0, 5) # a função randint() gera um número inteiro aleatório entre dois números.
numero = int(input('Em que número estou a pensar? '))

print('PROCESSANDO...')
sleep(2) # faz o programa aguardar dois segundos para executar o próximo comando!

if numero == sorte:
    print('Parabéns. Acertaste na mosca!')

else:
    print('Errado. Eu pensei no {} e não no {}. Tente novamente!'.format(sorte, numero))