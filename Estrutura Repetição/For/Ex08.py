"""Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."""

from datetime import date

ano_atual = date.today().year
maior = 0
menor = 0

for c in range(0, 7):
    ano_nascimento = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    idade = ano_atual - ano_nascimento
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'Dos anos digitados, {maior} já atingiram a maioridade e {menor} ainda não atingiram a maioridade!')

# Sei que deve existir outra forma de se fazer esse exercício, mas essa foi a lógica que melhor tive e que mais foi satisfatória de se pensar!