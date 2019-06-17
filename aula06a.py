'''
Exercicio 004
'''

n = input('Digite algo: ')
print(type(n))

n1 = input('Digite um número:')
n2 = input('Digite outro:')
s = n1+n2
print('A soma vale',s)

n1 = int(n1)
n2 = int(n2)
s = n1+n2
print('A soma entre {} e {} vale {}'.format(n1, n2, s))
print(f'A soma entre {n1} e {n2} vale {s}')
