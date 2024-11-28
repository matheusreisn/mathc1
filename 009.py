valor = []
pares = []
impar = []
for c in range (0, 999):
    n = int(input('Digite um valor: '))
    valor.append(n)
    if n % 2 == 0:
        pares.append(n)
    else: 
        impar.append(n)
    c = str(input('Quer continuar? [S/N] ')).lower()
    if c != 's':
        break
print (f'A lista completa é {valor}. ')
print (f'A lista de pares é {pares}')
print (f'A lista de impares é {impar}')