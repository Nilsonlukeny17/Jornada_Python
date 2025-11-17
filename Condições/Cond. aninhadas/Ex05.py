""" Crie um programa que leia duas notas de uma aluno e calcule a sua média, mostrando uma mensagem no final de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou supeirior: APROVADO"""

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
média = (n1 + n2) / 2

if média < 5.0:
    print('A sua média foi de {}. Estás REPROVADO!'. format(média))
elif média >= 5.0 and média < 7: # também posso fazer if 7 > média >= 5
    print('A sua média foi de {}. Estás em RECUPERAÇÃO!'.format(média))
elif média >= 7.0:
    print('A sua média foi de {}. Estás APROVADO!'.format(média))