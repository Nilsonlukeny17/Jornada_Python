"""Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer."""

from random import randint

print('Vou pensar num número entre 0 e 10. Tente adivinhar')
sorte_computador = randint(0, 10)
print(sorte_computador)
jogador = int(input('Qual é o número? '))
palpite = 0
while jogador != sorte_computador:
    nova_tentativa = int(input('Errado. Tente novamente: '))
    palpite += 1
if palpite < 3: # aqui foi só algo que pensei em implementar
    print(f'Estiveste bem. Apenas {palpite}')
else:
    print(f'Ao todo foram {palpite}. Estiveste mal.\n Precisas melhorar')