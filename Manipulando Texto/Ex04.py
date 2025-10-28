'''Escreva um programa que leia uma frase pelo teclado e mostre:
- quantas vezes aparece a letra 'A'.
- em que posição ela aparece a primeira vez.
- em que posição ela aparece a última vez.
'''
frase = str(input('Digite uma frase: ')).lower().strip()

print("A letra 'A' aparece {} vezes".format(frase.count('a')))
print("O primeiro 'a' aparece na posição {}".format(frase.find('a')+1)) # caso eu quisesse que a contagem começasse do indice 1, bastava colocar +1 depois do parentese do find (forma mais humana)
print("O segundo 'a' aparece na posição {}".format(frase.rfind('a')+1))# o "rfind" comeceça a contar da direita pra esquerda. Assim que ele encontra a primeira letra, imprimime como sendo a última. 

# Criando variáveis
print('\n') # Quebra a linha

n_de_vezes = frase.count('a')
primeira_vez = frase.find('a') +1
ultima_vez = frase.rfind('a') +1

print("A letra 'A' aparece {} vezes".format(n_de_vezes))
print("A letra 'A' aparece pela primeira vez na posição {}".format(primeira_vez))
print("A letra 'A' aparece pela última vez na posição {}".format(ultima_vez))