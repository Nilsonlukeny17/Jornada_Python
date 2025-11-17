""" A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER """
from datetime import date

ano_nascimento = int(input('Qual é o seu ano de nascimento? '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

print('Quem nasceu em {} tem {} anos'.format(ano_nascimento, idade))
if idade <= 9:
    print('Com base na tua idade, a tua categoria é MIRIM')
elif idade <= 14:
    print('Com base na tua idade, a tua categoria é INFANTIL')
elif idade <= 19:
    print('Com base na tua idade, a tua categoria é JUNIOR')
elif idade <= 25:
    print('Com base na tua idade, a tua categoria é SÊNIOR')
else:
    print('Com base na tua idade, a tua categoria é MASTER')