#Questão 05

A = []
B = []
for c in range (1, 51):
    n = int(input("Digite um número: "))
    if c <= 25:
        A.append(n)
    elif c >= 25:
        B.append(n)
      
def lista_C(A1, B1):
    C = []
    for a,b in zip(A1, B1):
        C.append(a)
        C.append(b)
    return C

C = lista_C(A, B)

print(f'{A}\n{B}\n{C}')


    




    
    
    
