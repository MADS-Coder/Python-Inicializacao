#Vinte-e-um

#Importa a biblioteca random.
from random import *

print('''
Vinte e um!
===========
Tente fazer exatamente 21 pontos!''')

#A varável recebe o booleano True
jogando = True
#A variavel é inicializada com o ZERO.
pontuacao = 0

#Usando o laço de repetição enquanto a variavel é verdadeira.
while jogando == True:
    numero = randint(1,10) #Mostra um numero aleatório entre 1 e 10.
    pontuacao += numero    #A variavel recebe ela mesma somada com a variavel numero.
    print("\nSeu próximo numero é", numero)#Mostra o próximo número
    print("Sua pontuação agora é", numero)#Mostra a pontuação atual.
    print("\nGostaria de somar mais um número?(s/n) ")
    resposta = input().lower()#A resposta idicada é convertida para minusculas.
    if resposta == 'n' or resposta == 'nao': #A condição de parada do loop é idicada pela respota se ela for igual a N,n ou nao.
        jogando = False #Se a condição for negativa, a variavel recebe o valor booleano negativo e sai do loop.
    
if pontuacao == 21:#A condição é que se a pontuação do jogador for igual a 21 ele vence.
    print("Sua pontuação final é", pontuacao)#Mostra a pontuação final caso ele vença.
    print("VOCÊ VENCEU!!")
else:#A condição é que se a pontuação do jogador for diferente de 21 ele perde.
    print("Sua pontuação final é", pontuacao)#Mostra a pontuação final caso ele perca.
    print("Que pena!!")
    
