valor = []
par = []
impar = []
for c in range (1,8):
    v = int(input(f'Digite o {c}. valor: '))
    valor.append(v)
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print (f'Os valores pares digitados foram {par}')
print (f'Os valores impares digitados foram {impar}')