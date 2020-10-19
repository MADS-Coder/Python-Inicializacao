#Questão 03

num = {}
lista = []
n = int(input('Qual a face do dado que quer jogar?: '))
num["face"] = n
lista.append(n)
cont = 1
#------------------------------------------------------------
while True:
    num.clear()
    n = int(input('Qual a face do dado que quer jogar?: '))
    num["face"] = n
    if num["face"] == 0:
        break
    lista.append(n)
    cont += 1
print(f'O dado foi lançado {cont} vezes.')
#------------------------------------------------------------
def remove(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l
res = remove(lista)
#------------------------------------------------------------
for c in res:
    m = lista.count(c)
    if cont != 1:
        print(f'A face {c} saiu {m} vezes.')
    else:
        for j in range(1, 7):
            if cont == 1:
                m = res.count(j)
                print(f'A face {j} saiu {m} vezes.')
