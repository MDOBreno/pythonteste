
# Desafio 005
n1 = float(input('Digite a primeira nota: '))
print(f'O antecessor é {n1 - 1}, \ne o sucessor é {n1 + 1}.')

# Desafio 006
print(f'O dobro é {n1 * 2}, \no triplo é {n1 * 3}, \ne a raiz quadrada é {(n1 ** (1 / 2)):.5f}')
print('\n')

# Desafio 007
n2 = float(input('Digite a segunda nota: '))
print(f'A média é {((n1+n2)/2):.2f}')

# Desafio 008
comp = float(input('\nDigite um comprimento em metros: '))
print(f'Seu valor em Centimetros é {comp*100} e {comp*1000} em milimetros.')

# Desafio 009
tabuada = float(input('\nDigite um valor para tabuada: '))
for x in range(1, 11):
    print(f'{tabuada} x {x:0>2} = {(tabuada*x)}')

# Desafio 010
reais = float(input('\nQuantos reais você tem na carteira? '))
print(f'Dá para você comprar US${(reais/3.27):.2f} dolares.')

# Desafio 011
altura = float(input('\nDiga a altura da parede: '))
largura = float(input('Diga a largura da parede: '))
area = (altura*largura)
litros = (area/2)
print(f'Para essa parede de {area:.2f}m2, serão necessarios {litros:.1f}L de tinta.')

# Desafio 012
precoOrig = float(input('Diago o preço original: '))
print(f'O valor dele com desconte é: {(precoOrig*0.95):.2f}')

# Desafio 013
salarioAtual = float(input('Qual o seu salario agora? '))
print(f'Parabens! Voca acaba de ganhar um aumento, e seu salario agora é de R${(salarioAtual*1.15):.2f}.')

