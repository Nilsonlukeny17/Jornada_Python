''' Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais'''

print('='*52)
print('Digite dois números para saber qual deles é o maior!')
print('='*52)

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

if n1 > n2:
    print('O maior número é {}'.format(n1))
elif n2 > n1:
    print('O maior número é {}'.format(n2))
else:
    print('Não existe maior valor. Os dois números são iguais!')