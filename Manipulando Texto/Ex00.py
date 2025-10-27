'''Crie um programa que leia o nome completo de uma pessoa e mostre:
- o nome com todas as letras maiusculas
- o nome com todas minusculas
- quantas letras tem ao todo (sem considerar espaços)
- quantas letras tem o primeiro nome
'''
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiusculas ficará {} '.format(nome.upper()))
print('Seu nome em minusculas ficará {}'.format(nome.lower()))
print('O nome {} tem {} letras'.format(nome, len(nome) - nome.count(' '))) # Vai ignorar os espaços encontrados
print('O primeiro nome tem {} letras'.format(nome.find(' '))) # Há uma outra forma de fazer isso!!
print('O primeiro nome tem {} letras'.format(len(nome.split()[0]))) # forma longa, mas foi a que melhor entendi.
# para imprimir o número de letras do segundo nome (assim por diante) faço assim:
print('O segundo nome é {} letras'.format(nome.split()[0]))

# Agora, vou fazer tudo isso criando variáveis para não colocar tudo dentro do print

maiusculas = nome.upper()
minusculas = nome.lower()
num_letras_sem_espaço = len(nome) - (nome.count(' '))
num_letras_prim_nome = len(nome.split()[0])
num_letras_seg_nome = len(nome.split()[1])

print(maiusculas)
print(minusculas)
print(num_letras_sem_espaço)
print(num_letras_prim_nome)
print(num_letras_seg_nome)