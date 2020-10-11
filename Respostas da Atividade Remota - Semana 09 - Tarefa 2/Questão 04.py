#Questão 04

matriz = []
a = 2012
anos = []
empresa = []
F = 'Fiat'
FO = 'Ford'
G = 'GM'
W = 'Wolkswagen'
#----------------------------------------------------------------------------
for l in range(0, 4):
    linha = []
    if l == 0:
        empresa.append(F)
    elif l == 1:
        empresa.append(FO)
    elif l == 2:
        empresa.append(G)
    elif l == 3:
        empresa.append(W)
    else:
        break
    for c in range(0, 6):
        num = (int(input(f'Digite valores para preencher a matriz [{l}, {c}]: ')))
        linha.append(num)
    matriz.append(linha)
ano = int(input("Digite um ano entre [2013 e 2018]: "))
#------------------------------------------------------------------------------
for n in range(0, 6):
    a += 1
    if a <= 2018:
        anos.append(a)
        print(f'[{anos[n]:^5}]',end='') 
    else:
        break
print()
#-------------------------------------------------------------------------------
'''O código abaixo identifica
o maior valor pelo ano informado'''
i = anos.index(ano)
mail = 0
maic = 0
mai = 0
maior = matriz[0][i]
for l in range(0, 4):
    for c in range(0, 6):
        if c == i:
            maior = matriz[l][i]
        if maior < matriz[l][i]:
            mail = l
            maic = i
            mai = matriz[mail][maic]
            e = empresa[l]
        elif i == 0:
            if maior <= matriz[l][i]:
                mail = l
                maic = i
                mai = matriz[mail][maic]
                e = empresa[l]
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
#---------------------------------------------------------------------------------
'''O código abaixo soma os valores por coluna/ano
e informa o ano de maior venda'''
many = 0
for c in range(6):
    somac = 0
    cont = 0
    for l in range(4):
        cont += 1
        somac += matriz[l][c]
        if cont == 0:
            many = somac
        else:
            if somac > many:
                many = somac
                a = anos[c]
#---------------------------------------------------------------------------------
print(f'A fabricante que mais vendeu em {ano} foi a {e} com {mai} mil unidades.')
print(f'O ano de maior volume geral de vendas foi {a} com {many} mil unidades.')
print('A média anual de vendas de cada fabricante entre 2013 e 2018 foi:')

'''O código abaixo realiza a média
dos valores por cada empresa'''
for l in range(4):
    somal = 0
    for c in range(6):
        somal += matriz[l][c]
    e = empresa[l]
    media = round(somal/6, 2)
    print(f'A {e} vendeu em média {media} unidades por ano.')













