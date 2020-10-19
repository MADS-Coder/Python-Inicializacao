#Questão 02

anos = {}
lista = []
#----------------------------------------------------------------------
#Realiza a pergunta mil vezes do ano
for c in range(1, 1001):    
        ano = int(input())
        anos["ano"] = ano
        lista.append(ano)
#----------------------------------------------------------------------
#Remove os itens duplicados e joga em uma nova lista de forma ordenada
def remove(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l
listas = remove(lista)
#----------------------------------------------------------------------
#Imprime os itens em ordem na vertical
for c in listas:
    n = lista.count(c)
    print(f'{c}: {n}')









