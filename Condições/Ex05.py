# Escreva um programa que leia três númeos e mostre qual é o maior e qual é o menor

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

# Verificando quem é menor
menor = n1 # Para facilitar, considerei já o n1 como sendo o menor. Isso facilita e reduz as condições. Assim praticamente vou trabalhar com duas opções.
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Verificando quem é maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor número é {}'.format(menor))
print('O maior número é {}'.format(maior))

