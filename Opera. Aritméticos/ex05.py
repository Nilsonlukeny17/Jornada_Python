#Conversor de Moedas

#Supondo que 1USD = 917kzs

kwz = float(input('Digite o valor em kwanza a ser convertido: '))
dolar = kwz / 917.00
print('{}kwz equivale a {:.2f}usd'. format(kwz, dolar))