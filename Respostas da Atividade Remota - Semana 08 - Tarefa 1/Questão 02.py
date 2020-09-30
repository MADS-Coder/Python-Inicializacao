#Questão 02

zero = []
lista1 = []
um_a_n = []
n = int(input("Digite um número: "))
t = (n*2)+2
lista1.append(n)
if n == 0:
    zero = []
    um_a_n = []
    l = []
    i = []
for z in range (1, lista1[0]+1):#Lista de m posições somente com ZEROS.(1)
    zero.insert(0, 0)
for m in range(1, lista1[0]+1):#Lista de m posições.(2)
    um_a_n.append(m)
    while len(lista1)+1 < t:
        n = int(input("Digite um número: "))
        lista1.append(n)
    if len(um_a_n) in lista1:#Lista restante da lista total.(3)
        l = lista1[1:len(um_a_n)+1]
    if len(um_a_n) in lista1:#Lista restante inversa.(4)
        i = lista1[len(um_a_n)+1:]
        i = i[::-1]
    
print(f'{zero}\n{um_a_n}\n{l}\n{i}')
    




    
    
    
