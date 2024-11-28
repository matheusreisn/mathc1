import random
n = tuple(random.sample(range(0, 10), 5))
print (f'Os valores sorteados foram {n}')
print (f'O maior valor sorteado foi {max(n)}')
print (f'O menor valor sorteado foi {min(n)}')