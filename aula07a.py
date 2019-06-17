'''
Aula 007-A
'''

nome = str(input('Qual é o seu nome? '))
print(f'Prazer em te conhecer {nome:>20}!')
print(f'Prazer em te conhecer {nome:<20}!')
print(f'Prazer em te conhecer {nome:^20}!')
print(f'Prazer em te conhecer {nome:=^20}!')

# -------------------------------------------

n1 = int(input('Um valor:  '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f'A soma á {n1+n2}, \n o produto é {n1*n2}, \n e a divisão é {n1/n2}, ', end='')
print(f'Divisão inteira {n1//n2} e potência {n1**n2}')
print(f'A soma á {s}, \n o produto é {m}, \n e a divisão é {d:.3}, ', end='')
print(f'Divisão inteira {di} e potência {e}')
