#Pintando Parede

"""
Escreva um programa que leia a largura e altura da parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que a cada litro de tinta pinta uma área de 2m²
"""
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
área = largura * altura
tinta = área / 2 #Estava um pouco dificil pegar isso, mas é só matemática mesmo! Já peguei.
print('A parede tem a dimensão de {:.0f}x{:.0f} e a sua área é de {}m²'.format(largura, altura, área))
print('Para pintar uma parede de {}m² serão necessários {}l de tinta'.format(área, tinta))