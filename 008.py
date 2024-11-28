valor = []
soma = 0
for c in range (0, 999):
    n = int(input('Digite um valor: '))
    valor.append(n)
    c = str(input('Quer continuar? [S/N] ')).lower()
    if c != 's':
        break
if n == 5:
    print ('O valor 5 faz parte dessa lista! ')
else:
    print ('O valor 5 não faz parte dessa lista! ')
print (f'Você digitou {len(valor)} elementos. ')
valor.sort(reverse=True)
print (f'Os valores em ordem decrescente são {valor} ')