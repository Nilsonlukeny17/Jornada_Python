# Escreva um programa que leia um ano qualquer e mostre se ele é bissexto.

# Ano bissexto, matematicamente, são aqueles que o resto da divisão do ano por 4 dá 0
# Mas com algumas excepções: se também for divisivel por 100, não é bissexto. Se for divisivel por 400, volta a ser bissexto!

'''Ou seja, se o resto por 4 for 0, ela entra na lista dos bissextos.
Se o resto por 100 for diferente de 0 (for divisivel), ela sai da lista dos bissextos.
Mas se o resto por 400 for igual a 0, ela entra novamente na lista dos anos bissextos'''
from time import sleep
from datetime import date # Importei essa biblioteca para fazer o computador ler o ano atual

ano = int(input('Que ano quer analisar? Digite 0 se quiser analisar o ano atual: '))
print('Analisando...')
sleep(1)

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
    
else:
    print('O ano {} NÃO É BISSEXTO'.format(ano))