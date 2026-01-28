"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto."""


sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF': # loop só roda se não tiver M ou F em sexo. Se tiver, ela pula para o outro comando (lógico) - Ele praticamente diz 'enquanto sexo não for M ou F, entre!'
    sexo = str(input('Opção errada. Tente novamente: ')).strip().upper()[0]
print(f'Sexo {sexo} registado com sucesso!')