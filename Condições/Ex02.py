# Escreva um programa que leia um número inteiro e mostre na tela se é par ou ímpar

numero = int(input('Digite um número: '))
resultado = numero % 2

if numero == 0:
    print('O número é PAR')
else:
    print('O número é ÍMPAR')