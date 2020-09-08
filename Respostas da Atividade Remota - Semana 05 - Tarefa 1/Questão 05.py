#Questão 05
from random import randint
def maior(num):
    cont = 0
    for num in range(1, 101):
        n = randint(1, 1000)
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont += 1
    print(f'\n\nVocê digitou um número que formou um conjunto de {cont} números,\nno qual o maior deles é {maior}.')        
def main():
    numero = int(input('Digite um número: '))

    result = maior(numero)
    
if __name__=='__main__':
    main()

    

