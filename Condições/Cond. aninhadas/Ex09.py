""" Elabore um programa que calcule o valor a ser pago pela compra feita, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto [pagamento no momento]
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal [pagamento a prazo]
- 3x ou mais no cartão: 20% de juros"""

print('=' * 10, 'Lojas LUKENY', '=' * 10)
preço = float(input('Qual é o preço das compras? '))
print("""FORMA DE PAGAMENTO:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] até 2x no cartão
[ 4 ] até 3x ou mais no cartão""")
escolha = int(input('Qual é a opção? '))

if escolha == 1:
    novo_preço = preço - (preço * (10 / 100))
    print(f"A compra que fizeste de {preço:.0f} kzs, ficará a {novo_preço_1:.0f} kzs com desconto!")
elif escolha == 2:
    novo_preço = preço - (preço * (5 / 100))
    print(f"A compra que fizeste de {preço:.0f} kzs, ficará a {novo_preço_1:.0f} kzs com desconto!")
elif escolha == 3:
    novo_preço = preço
    num_parcelas = preço / 2
    print(f"A compra que fizeste será parcelada em 2x de {num_parcelas}")
elif escolha == 4:
    parcelas = int(input('Quantas vezes quer parcelar? '))
    novo_preço = preço + (preço * (20 / 100))
    preço_com_num_parcelas = novo_preço / parcelas
    print(f"A compra que fizeste será parcelada em {parcelas}x de {preço_com_num_parcelas} ")
else:
    print('Opção Errada. Tente novamente!!')

    