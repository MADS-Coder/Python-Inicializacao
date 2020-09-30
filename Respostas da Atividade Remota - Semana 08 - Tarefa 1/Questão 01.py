#Questão 01

lista = []
soma = 0
mult = 1
for n in range(1, 11):
    num = int(input("Digite um número: "))
    lista.append(num)
    soma += num
    mult *= num

print(f'{lista}\n{soma}\n{mult}')
    
    
    
