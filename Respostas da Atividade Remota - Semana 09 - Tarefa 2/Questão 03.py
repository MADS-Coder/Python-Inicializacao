#Questão 03

lin = int(input("Digite um numero de linhas da matriz: "))
col = int(input("Digite um numero de colunas da matriz: "))
matriz = []
soma = somal = somac =  menor = maior = cont = 0
for l in range(0, lin):
    linha = []
    for c in range(0, col):
        cont += 1
        num = int(input(f'Digite um número para [{l}][{c}]: '))
        linha.append(num)
        soma += num
        if cont == 1:
            maior = menor = num
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num
                
    matriz.append(linha)
'''------------------------------------------------------------'''    
media = round(soma/(lin*col), 4)

'''------------------------------------------------------------''' 
for l in range(0, lin):
    for c in range(0, col):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()

'''------------------------------------------------------------''' 
for c in range(0, col):
    somal += matriz[0][c]

'''------------------------------------------------------------''' 
for l in range(0, lin):
    somac += matriz[l][c]

print(f'({somal}, {somac}, {media}, {menor}, {maior})')    

