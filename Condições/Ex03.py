''' Cria uma programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando 3 USD por Km para viagens de até 200Km e 1.5 USD para viagens mais longas devido a uma promoção '''

distancia = float(input('Qual distancia vais percorrer? '))
print('Vais percorrer uma distância de {}'.format(distancia))

if distancia <= 200:
    preco = distancia * 3
else:
    preco = distancia * 1.5
print('O valor total a pagar pela viagem será {} USD'.format(preco))

