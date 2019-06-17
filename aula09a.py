
frase = 'Curso em Vídeo Python'

print(frase[::2])
print("""Welcome! Are you completely new to programming? 
If not then we presume you will be looking for information 
about why and how to get started with Python. Fortunately an 
experienced programmer in any programming language (whatever it 
may be) can pick up Python very quickly. It's also easy 
for beginners to use and learn, so jump in!""")
print(frase.count('o'))
print(frase.count('O'))
print(frase.upper().count('O'))
print(len(frase))

frase = '   Curso em Vídeo Python   '
print(len(frase))
print(frase.strip())

frase = 'Curso em Vídeo Python'
print(frase.replace('Python', 'Android'))
print(frase)
print('Curso' in frase)
print(frase.find('Vídeo'))
print(frase.find('vídeo'))
print(frase.lower().find('vídeo'))
dividido = frase.split()
print(dividido)
print(dividido[0])
print(dividido[2][3])

