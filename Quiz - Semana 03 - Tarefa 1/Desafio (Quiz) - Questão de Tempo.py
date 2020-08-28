#DESAFIO QUIZ
#Questão de Tempo

from time import sleep

print('-=' * 30)
print('               DESAFIO DO ADIVINHO          ') 
print('-=' * 30)
print('''Está preparado?
1 - [SIM]
2 - [NÃO]''')
resp = int(input('Digite uma opção: '))

if resp == 1:
    print('Vamos la...')
    sleep(0.9)
    print('Qual o animal que come com o rabo?')
    print('''
    [a] - Raposa.
    [b] - Cachorro.
    [c] - Todos, pois não podem tirar para comer.
    [d] - Jumento.
    [e] - Galinha.
          ''')
    resposta = input('Qual sua resposta: ')
    
    while resposta != 'c':
        print('Que pena :( a resposta está errada...Tente novamente.')
        resposta = input('Qual sua resposta: ')
        
    if resposta == 'c':
        print('UUUUURRRRRUUUU PARABÉNSSSSSSSS.......você acertou :) :) :)')
else:
    print('Obrigado por participar :)')

while resp != 1 and resp != 2:
    print('Opção inválida...Digite novamente')
    resp = int(input('Digite uma opção: '))
    if resp == 1:
        print('Vamos la...')
        sleep(0.9)
        print('Qual o animal que come com o rabo?')
        print('''
        [a] - Raposa.
        [b] - Cachorro.
        [c] - Todos, pois não podem tirar para comer.
        [d] - Jumento.
        [e] - Galinha.
              ''')
        resposta = str(input('Qual sua resposta: '))
    
    while resposta != 'c':
        print('Que pena :( a resposta está errada...Tente novamente.')
        resposta = input('Qual sua resposta: ')
        
    if resposta == 'c':
        print('UUUUURRRRRUUUU PARABÉNSSSSSSSS.......você acertou :) :) :)')
        
    elif resp == 2:
        print('Obrigado por participar :)')
    break
    
