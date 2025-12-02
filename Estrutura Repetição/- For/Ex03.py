# Refaça o DESAFIO 009  (Tabuada), mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Digite um número para ver a sua tabuada: '))
for tabuada in range (1, 11):
    multi = num * tabuada
    print(f'{num} X {tabuada} = {multi}')