print('\033[7;33;44mOlá, Mundo!\033[m')

a = 3
b = 5
print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}\033[m!!!')

nome = 'Guanabara'
nomeAbre = '\033[4;34;m'
nomeFecha = '\033[m'
print(f'Olá! Muito prazer em te conhecer, {nomeAbre}{nome}{nomeFecha}!!!')

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print(f'Olá! Muito prazer em te conhecer, {cores["pretoebranco"]}{nome}{cores["limpa"]}!!!')


