from math import sqrt, floor, trunc, radians
import random

num = int(input('Digite um número: '))
raiz = sqrt(num)
print(f'A raiz de {num} é igual a  {floor(raiz)} (arredondamento pra baixo de {raiz}) .')

# --------------------------------------------------------------------


num = random.random()
print(num)
num = random.randint(1,10)
print(num)

# --------------------------------------------------------------------

import emoji

print(emoji.emojize('Olá, Mundo :smiling_face_with_sunglasses:', use_aliases=True))

# --------------------------------------------------------------------

# Desafio 016
valor = float(input('Insira um valor Real: '))
print(f'A parte inteira é {trunc(valor)}')

# Desafio 017
ca = float(input('Insira o valor do cateto adjacente: '))
co = float(input('Insira o valor do cateto oposto: '))
hipo = sqrt((ca**2)+(co**2))
print(f'A hipotenusa é: {hipo:.3f}')

# Desafio 018
import math
angulo = radians(float(input('Insira um angulo: ')))
print(f'O seno é {math.sin(angulo)} \nO cosseno é {math.cos(angulo)} \nA tangente é {math.tan(angulo)}')


# Desafio 019
a1 = input('Nome do Aluno 1: ')
a2 = input('Nome do Aluno 2: ')
a3 = input('Nome do Aluno 3: ')
a4 = input('Nome do Aluno 4: ')
x = random.randint(1,4)
aluno = ''
if x == 1:
    aluno = a1
elif x == 2:
    aluno = a2
elif x == 3:
    aluno = a3
else:
   aluno = a4
print(f'O aluno sorteado foi {aluno}')




