# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

""" Passos:
Ler o nome, idade e sexo de 4 pessoas
mostrar a média
nome do mais velho
mulheres com menos de 20 anos"""

soma_idade = 0 # Variável para receber o valor da soma de todas as idades
média_idade = soma_idade / 4 # Calculando a média
maior_idade_homem = 0 # Variável que recebe a maior idade do homem
nome_mais_velho = '' # Variável que recebe o nome do homem mais velho
mulheres_menos_20anos = 0 # Variável que recebe o nº de vezes que a idade das mulheres for inferior a 20
for c in range(1, 5):
    print(f'------ {c}ª Pessoa ------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    soma_idade += idade
    if c == 1 and sexo == 'M': # Estou basicamente a dizer que se o c estiver na posição 1 (for igual a 1), execute os comandos abaixos
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo == 'M' and idade > maior_idade_homem: #Aqui estou a dizer que "se o sexo ainda for igual a M"
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo == 'F' and idade < 20: # Aqui a estou a dizer que se o sexo for igual a f e a idade menor que 20, a variável acomuladora vai receber +1
        mulheres_menos_20anos += 1
print(f'A média de idade do grupo é {média_idade} anos')
print(f'O nome do homem mais velho é {nome_mais_velho}, e ele tem {maior_idade_homem} anos')
print(f'Existem {mulheres_menos_20anos} com menos de 20 anos')
