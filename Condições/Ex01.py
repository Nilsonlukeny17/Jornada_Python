'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre a mensagem dizendo que ele foi multado.
A multa vai custar 10 usd por cada km acima do limite'''

velocidade = float(input('Qual é a velocidade atual do carro? '))

multa = (velocidade - 80) * 10

if velocidade > 80:
    print("""Foste multado. Excedeste a velocidade recomendada de 80km/h!\nVais pagar uma multa de {} usd """.format(multa))

else:
    print('Continue dirigindo assim!')