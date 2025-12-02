# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

# Lembrando mais uma vez que números pares são aqueles que o resto da divisão por 2 é 0. Divisão exata!!

soma = 0
for num in range(1, 7):
    números = int(input('Digite um número: '))
    if números % 2 == 0:
        soma += números
print(f'A soma dos números pares digitados é {soma}')
