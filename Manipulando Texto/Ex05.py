# Escreva um programa que receba o nome completo de uma pessoa e mostre o primeiro e último nome

nome_comp = str(input('Digite seu nome completo: ')).strip().split()

print("O primeiro nome é '{}'".format(nome_comp[0]))
print("O último nome é '{}' ".format(nome_comp [-1])) #índices negativos começam a contar a partir do fim. Nesse caso eu chamei o que está no fim!

# Adivinha só?
# Com variáveis
print("\n")

primeiro_nome = nome_comp[0]
ultimo_nome = nome_comp[-1]

print("O primeiro nome é {}".format(primeiro_nome))
print("O último nome é {}".format(ultimo_nome))