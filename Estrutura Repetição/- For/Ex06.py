# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

# número primo é um número que só pode ser dividido por 1 e por ele mesmo, sem deixar resto
num = int(input('Digite um número inteiro: '))

total = 0
for c in range(1, num  + 1):
    if num % c == 0:
        print('\033[33m', end= '') # amarelo
        total += 1
    else:
        print('\033[31m', end='') # vermelho
    print(f'{c}', end=' ')
print(f'\n\033[mO número {num} foi divisível {total} vezes.')
if total == 2: # essa é a condição para verificar se é primo, uma vez que primo só há duas condições: divisível por 1 e por ele mesmo!
    print(f'Por isso ele é PRIMO!')
else:
    print(f'Por isso ele NÃO é PRIMO!')

# não te assustes com os números! São apenas cores para a saída.

#forma sem cores

