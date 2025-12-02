# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split() # usei o split para separar cada palavra. É como se elas fossem um tomate e agora cortei esse tomate em pedaços e guardei num saco. No caso, o saco é a variável 'palavra'
junto = ''.join(palavra) # agora usei o ''.join para juntá-las sem nada. Como dentro das aspas não tem nada, ela vai fazer as palavras estarem juntas, sem espaço!!
inverso = '' # nesse momento a variável está vazia. NÃO TEM NADA!!
for letra in range(len(junto) - 1, -1, -1): # loop para percorrer a lista de trás para frente: len(lista) -1 -> pega o último elemento da string; -1 -> porque quero incluir o valor na posição 0; -1 -> passo que dou, vai andar para trás, recuando uma casa!
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('É um Palíndromo')
else:
    print('Não é um Palíndromo')

# O que ficou guardado nesse exercício foi ter entendido mais uma vez como fazer o inverso de alguma coisa usando o loop for!!
# se não tivesse que usar o loop, poderia simplesmente criar mais uma variável inverso e lhe fazer receber junto[::-1], assim digo para começar no inicio, terminar no fim e voltar 1