""" Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes """

r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('As retas inseridas formam um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    if r1 == r2 != r3:
        print('ISÓSCELES')
    if r1 != r2 != r3:
        print('ESCALENO')
else:
    print('As retas inseridas não formam um triângulo!!')