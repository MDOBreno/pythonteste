

nome = str(input('Qual é seu nome? '))
if 'BRENO' in nome.upper():
    print('Que nome lindo você tem!')
print(f'Bom dia {nome}')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'A sua média foi {m:.1f}')
if m >= 6.0:
    print('Sua nota foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
print('PARABÉNS!' if m >= 6.0 else 'ESTUDE MAIS!')







