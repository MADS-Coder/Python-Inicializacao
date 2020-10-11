#Questão 01

n = int(input("Digite um número: "))
matriz = []
for l in range(0, n):
    linha = []
    for c in range(0, n):
        num = int(input(f'Digite um número para [{l}][{c}]: '))
        linha.append(num)
    matriz.append(linha)
maior = matriz[0][0]
menor = matriz[0][0]
maior_linha = 0
maior_coluna = 0
menor_linha = 0
menor_coluna = 0
for l in range(0, n):
    for c in range(0, n):
        if maior < matriz[l][c]:
            maior = matriz[l][c]
            maior_linha = l
            maior_coluna = c
        if menor > matriz[l][c]:
            menor = matriz[l][c]
            menor_linha = l
            menor_coluna = c 
        print(f'[{matriz[l][c]:^5}]', end='')
    print()        
print(f'O maior valor está na posição ({maior_linha}, {maior_coluna})\nO menor valor está na posição ({menor_linha}, {menor_coluna})')









 


