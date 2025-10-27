# Sorteado uma ordem na lista

'''O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um prograna que leia o nome dos quatro alunos e mostre a ordem sorteada'''

import random
'''
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo alunno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto alunno: '))
lista = [n1, n2, n3, n4]
sorte = random.shuffle(lista)

print('A ordem dos alunos será {}'.format(sorte)) ---- # Deu None! Preciso entender porquê que isso aconteceu!
'''
'''Deu none porque a função shuffle não cria nada. Ela simplesmente pega em algo existente e embaralha, ou seja, 
ao lhe colocar dentro de uma variavel estamos a criar uma sorte, mas nela não cria. Para mostrar a sorte, tem que chamar a variavel que mostra a 
lista dos nomes que no caso virá já sorteada.'''

# A forma correta é essa: 
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo alunno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto alunno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)

print('A ordem dos alunos será {}'.format(lista)) # Imprimos a própria lista que foi baralhada, sem precisar criar nada