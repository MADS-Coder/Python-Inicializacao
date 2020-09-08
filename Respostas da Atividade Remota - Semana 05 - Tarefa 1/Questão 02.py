#Questão 02

from random import randint
par = impar = soma = 0
num = int(input('Digite um numero entre: '))
for n in range(1, 101):
    numero = randint(1, 1000)
    print(numero)
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1

print(f'\n\nO número que você digitou produziu um conjunto de 100 números, dos quais\n{par} são pares e {impar} são ímpares.')


