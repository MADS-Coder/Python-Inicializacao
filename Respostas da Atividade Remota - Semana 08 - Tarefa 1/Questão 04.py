#Questão 04


lista = []
par = []
impar = []
for z in range (1, 21):
    n = int(input("Digite um número: "))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    elif n % 2 == 1:
        impar.append(n)
   
print(f'{lista}\n{par}\n{impar}')
    




    
    
    
