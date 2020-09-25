#Questão 02

n = int(input("Digite um número acima ou igual a [2] que mostrar a quantidade de termos que desejar: "))
t1 = 0
t2 = 1
cont = 3
print(f'{t1}, {t2}',end='')
while cont <= n:
    t3 = t1+t2
    print(f', {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1

        
