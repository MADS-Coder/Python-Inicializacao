#Consertando a entrada

from random import *

print('''
Porta da Fortuna!
=========

Existe um super prêmio atrás de uma destas 3 portas!
Adivinhe qual é a porta certa para ganhar o prêmio!

    _____      _____      _____ 
   |     |    |     |    |     |
   | [1] |    | [2] |    | [3] |
   |    º|    |    º|    |    º|
   |_____|    |_____|    |_____|
''')

score = 0
jogando = True
while jogando == True:
    portaEscolhida = int(input("\nEscolha das portas [1, 2 ou 3]: "))
    portaCerta = randint(1,3)
    print("A porta escolhida foi a", portaEscolhida)
    print("A porta certa é a", portaCerta)
    
    if portaEscolhida == portaCerta:
        score += 1
    else:
        print("Que peninha!")

    print(f'A sua pontuação é {score}.')

    print("\nVocê quer jogar de novo? (s/n) ")
    resposta = input().lower()

    if resposta == 'n' or resposta == 'nao':
        jogando = False
print("Obrigado por jogar.")
print("Sua pontuação final é de", score)
