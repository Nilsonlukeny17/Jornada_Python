'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.'''

valor_casa = float(input('Qual é valor da casa? '))
salário = float(input('Qual é o salário do comprador? '))
anos_a_pagar = int(input('Em quantos anos vai pagar? '))

# Aqui é para saber o valor da prestação mensal
prestação = valor_casa / (anos_a_pagar * 12) # transformei os anos em meses, e dividi o valor da casa pelo meses, para saber exatamente quanto pagarei por cada mês

# Aqui é a condição de exceder 30%
if prestação > salário * 30 / 100:
    print('Para teres uma casa de {} kzs em {} anos a prestação da casa será de {} kzs mensal!'.format(valor_casa, anos_a_pagar, prestação))
    print('Empréstimo NÃO pode ser feito. Seu pobre')
else:
    print('Para teres uma casa de {} kzs em {} anos a prestação da casa será de {} kzs mensal!'.format(valor_casa, anos_a_pagar, prestação))
    print('Empréstimo Pode ser feito. Tens kumbú!!')
