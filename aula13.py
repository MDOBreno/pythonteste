
for c in range(0, 7):
    print(c)
print(f'FIM\n')

for c in range(6, 0, -1):
    print(c)
print(f'FIM\n')

for c in range(0, 7, 2):
    print(c)
print(f'FIM\n')

# -----------------------------------

n = int(input('Digite um número: '))

for c in range(0, n+1):
    print(c)
print(f'FIM\n')

# -----------------------------------

i = int(input('Digite o Início: '))
f = int(input('Digite o Fim: '))
p = int(input('Digite o passo: '))

for c in range(i, f, p):
    print(c)
print(f'FIM\n')

# -----------------------------------

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print(f'O somatório de todos os vaçlores foi {s}')
print(f'FIM\n')


