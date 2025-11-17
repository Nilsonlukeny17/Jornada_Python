''' Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ela ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento.Seu programa também deverá mostrar o tempo que falta ou que passou do prazo'''

from datetime import date

ano_nascimento = int(input('Qual é o seu ano de nascimento? '))
ano_atual = date.today().year

ano_da_pessoa = ano_atual - ano_nascimento
tempo_que_falta = 18 - ano_da_pessoa
tempo_excedido = ano_da_pessoa - 18

print('Quem nasceu em {} tem {} em {}'.format(ano_nascimento, ano_da_pessoa, ano_atual))

if ano_da_pessoa < 18: # Se ainda vai
    print('Ainda vais te alistar')
    print('Nesse preciso momento faltam {} anos para te alistares!'.format(tempo_que_falta))
    ano = ano_atual + tempo_que_falta # para saber o ano exato que a pessoa estará apta para se alistar
    print('Seu alistamento será em {} anos(s).'.format(ano))
elif ano_da_pessoa == 18: # Se é o momento
    print('Esse é o momento exato para te alistares!!')
else: # Se já passou
    print('Já passaste da fase de alistamento.')
    print('Passaram-se {} anos da idade certa para te alistares!'.format(tempo_excedido))
    ano = ano_atual - tempo_excedido # para saber o ano exato que a pessoa esteve apta para se alistar
    print('Seu alistamento foi em {} ano(s).'.format(ano))