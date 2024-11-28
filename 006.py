valor = []
for c in range (0,999):
    numero = str(input('Digite um valor: '))
    valor.append(numero)
    print ('Valor adicionado com sucesso')

    continuar = (str(input('Quer continuar? [S/N] '))).lower()
    if continuar != 's':
        print ('Programa encerrado! ')
        break
num1 = sorted(valor)
print (f'Voce digitou os valores {num1}')