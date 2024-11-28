n = []
for c in range (0, 5):
    v = int(input('Digite um valor para a posição: '))

    n.append(v)
maior = max(n)
menor = min(n)
print (f'Voce digitou os valores {n}')
print (f'O maior numero digitado foi {maior}')
print (f'O menor numero digitado foi {menor}')