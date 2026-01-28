'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

primeiro = int(input('Qual é o primeiro valor? '))
segundo = int(input('Qual é o segundo valor? '))
escolha = 0
maior = primeiro
while escolha != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    escolha = int(input('Qual é a tua escolha? '))
    if escolha == 1:
        soma = primeiro + segundo
        print(f' O resultado de {primeiro} + {segundo} é {soma}')
        print('#' * 27)
    elif escolha == 2:
        multiplicação = primeiro * segundo
        print(f'O resultado de {primeiro} x {segundo} é {multiplicação}')
        print('#' * 27)
    elif escolha == 3:
        if segundo > primeiro:
            maior = segundo
            print(f'O maior número entre {primeiro} e {segundo} é {maior}')
            print('#' * 27)
        elif primeiro == segundo:
            print('Os números são iguais!')
            print('#' * 27)
    elif escolha == 4:
        novo_num1 = int(input('Qual é o primeiro valor? '))
        novo_num2 = int(input('Qual é o segundo valor? '))
        primeiro = novo_num1
        segundo = novo_num2
        print('#' * 27)
if escolha == 5:
    print('Número incorrecto. Tente novamente!')