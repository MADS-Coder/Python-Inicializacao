#Questão 03

from random import randint
n = int(input('Digite um número: '))
soma = 0
for m in range(1, 101):
    num = randint(n, 1000)
    soma += num

media = round(soma / m, 2)
print(f'\n\nVocê digitou um número, que formou um conjunto de 100 números, a soma dos mesmos é {soma},\nE a média é {media}.') 
