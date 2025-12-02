# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.


# Pensei numa lógica bem grande para resolver esse exercício que acabei por não conseguir. Afinal era algo simples!
print('=' * 30)
print('     10 Termos de uma PA    ')
print('=' * 30)

primeiro_termo = int(input('Primeiro Termo: '))
razão = int(input('Razão: '))

décimo = primeiro_termo + (10 - 1) * razão # fórmula matemática para encontrar o n termo de uma PA. O 10 pode ser substituido de acordo aos termos pedidos na PA

for pa in range(primeiro_termo, décimo + 2, razão): # o que mais gostei nesse exercício é que me ensinou que dentro de um range podem entrar variáveis! Mas sempre seguindo a lógica de (início, fim, passo)
    print(f'{pa}', end=' -> ')
print('Acabou!')