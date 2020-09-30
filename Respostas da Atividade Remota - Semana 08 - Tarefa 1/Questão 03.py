#Questão 03

lista = []
notas = []
letras1 = []
letras = []
min = []
n = float(input("Digite um número: "))
t = (n*1)+1
lista.append(n)
cont = 1
if n == 0:
    i = []
    notas = []
    media = "SEM NOTAS"
    minu = 0
    l = []
while cont < t:
    cont += 1
    n = float(input("Digite um número: "))
    lista.append(n)
    i = lista[1:]
    i = i[::-1]
soma = mai = minu = 0
for m in range(1,cont):
    nota = float(input("Digite a nota do aluno: "))
    notas.append(nota)
    soma += nota
    media = (soma/m)      
for m in range(1,cont):
    letra = str(input("Digite qualquer letra maiúscula ou minúscula: "))[0]
    l = letras.append(letra)
    if letra.lower() == letra:
        letras1.append(letra)
        minu = len(letras1)
        l = letras[1:3]
    else:
        l = letras[0:]
print(f'{i}\n{notas}\n{media}\n{minu}\n{l}')
