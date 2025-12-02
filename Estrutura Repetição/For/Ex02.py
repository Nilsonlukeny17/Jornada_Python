# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

# múltiplos de 3 são números que o resto da multiplicação de um número por 3 é 0. Ou seja, a divisão é exata!

# dividir por etapas: 
# loop for com números ímpares, 
# múltiplos de 3 e 
# depois soma!


soma = 0 # Precisei usar acomulador!!
contador = 0
for num in range (1, 501, 2): # ímpares
    if num % 3 == 0: # múltiplos de 3
        soma += num # somar todos os números múltiplos de 3
        contador += 1 # contar quantos números múltiplos de 3 tem!
print(f'Os números contados foram {contador} e a soma desses números é {soma}')