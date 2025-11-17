""" Escreva um programa que faça o computador jogar Pedra, Papel e Tesoura"""

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
# print(itens[computador]) -- o comando dentro do print serve para imprimir não os indices, mas sim as palavras dentro da variavel itens. Se tivesse só computador, aí a impressão seria números (os índices no caso!).

print("""Opções: 
[ 0 ] - Pedra
[ 1 ] - Papel
[ 2 ] - Tesoura""")
jogador = int(input('Então, qual vai ser a tua jogada? '))

# Pausa de 1 segundo para Pedra, Papel, Tesoura
print('Pedra')
sleep(1)
print('Papel')
sleep(1)
print('Tesoura')
sleep(1)

# Imprimir o resultado da escolha do jogador e do computador
print('=*=' * 8)
print(f'O computador jogou {itens[computador]}')
print(f'Você jogou {itens[jogador]}')
print('=*=' * 8)

# Condição para saber quem venceu!
if computador == 0: # computador jogou pedra
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('Parabéns. Venceste o computador!')
    elif jogador == 2:
        print('Boelo. Perdeste para uma máquina!')
    else:
        print('Jogada Inválida')
elif computador == 1: # computador jogou papel
    if jogador == 1:
        print('Empate!')
    elif jogador == 0:
        print('Boelo. Perdeste para uma máquina!')
    elif jogador == 2:
        print('Parabéns. Venceste o computador!')
    else:
        print('Jogada Inválida')
elif computador == 2: # computador jogou tesoura
    if jogador == 2:
        print('Empate!')
    elif jogador == 0:
        print('Parabéns. Venceste o computador!')
    elif jogador == 1:
        print('Boelo. Perdeste para uma máquina!')
    else:
        print('Jogada Inválida')
else:
    print('Opção Errada! Tente Novamente')