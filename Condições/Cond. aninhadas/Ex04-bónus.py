''' Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ela "ainda vai se alistar" ao serviço militar, se "é a hora de se alistar" ou se "já passou do tempo do alistamento". Seu programa também deverá mostrar o tempo que falta ou que passou do prazo. O programa também deverá ser capaz de ler o sexo e continuar se for masculino, mas terminar se for feminino.
'''
from datetime import date
from time import sleep

print('='*64)
print('Esse é um programa para verificar se uma pessoa pode se alistar.')
print('='*64)

verificação = int(input("""Mas antes de prosseguir, digite o seu sexo: 
[ 1 ] - Masculino
[ 2 ] - Feminino
: """).capitalize())

if verificação == 1:
    print('Aguarde 1 segundo...')
    sleep(1)
elif verificação == 2 :
    print('Mulheres não precisam se alistar! Fique tranquila!!') #Preciso descobrir uma forma de fazer o programa parar caso a pessoa seja do sexo feminino!


ano_nascimennto = int(input('Qual é o seu ano de nascimento? '))
ano_atual = date.today().year
idade =   ano_atual - ano_nascimennto
tempo_que_falta = 18 - idade
tempo_excedido = idade - 18

if idade < 18:
    print('Você ainda não tem a idade certa para se alistar.\nSeu alistamento será daqui a {} ano(s).'.format(tempo_que_falta))
    ano = ano_atual + tempo_que_falta
    print('Seu alistamento será em {}'.format(ano))
elif idade == 18:
    print('Você deve se alistar IMEDIATAMENTE.')
elif idade > 18:
    print('Você ja passou do tempo de alistamento.\nSeu alistamento foi há {} ano(s).'.format(tempo_excedido))
    ano = ano_atual -tempo_excedido
    print('Seu alistamento foi em {}'.format(ano))

# Voltarei quando descobrir!
