# Verificando as primeiras letras de um texto

# Escreva um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'

cidade = str(input('Digite a sua cidade: ')).strip()
print('Santo' in cidade.capitalize()) # O capitalize é para o programa aceitar qualquer forma que a palavra 'Santo' for escrita.
