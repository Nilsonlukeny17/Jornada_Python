# Verificando as primeiras letras de um texto

# Escreva um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'

cidade = str(input('Digite a sua cidade: ')).strip()
print('Santo' in cidade.capitalize()) # O capitalize é para o programa colocar o primeiro S em maiusculo e o resto em minusculo. 
# Assim, mesmo que tiver Santo (não no principio), o programa retornará false porque o capitalize fê-lo ficar minusculo.
