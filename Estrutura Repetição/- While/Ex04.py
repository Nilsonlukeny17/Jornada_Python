# Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

num = int(input('Digite um número para calcular o seu factorial: '))
c = num
f = 1
print (f'Calculando o {num}! ')
while c > 0:
    print(f'{c} ', end='')
    if c > 1:
        print('x ', end='')
    else:
        print('= ', end='')
    f *= c
    c -= 1
print(f'{f}')

# Utilizando o for para fazer esse exercicio, eu disse apenas ao f*= num para multiplicar todos os valores que estão no intervalo de 5 a 1 (valores de num)
f = 1
for num in range(5, 0, -1):
    print(f'{num} ', end='')
    if num > 1:
        print('x ', end='')
    else:
        print('= ', end='')
    f *= num
print(f'{f}')